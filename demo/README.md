LICITRA Demo – Runtime Integrity Walkthrough (Multi-Org)

This demo demonstrates:

deterministic SHA-256 hash chaining

tamper detection with exact failure index

multi-organization isolation

JSON + PDF evidence export

These artifacts prove LICITRA’s runtime integrity behavior.

Prerequisites

LICITRA core running locally

PostgreSQL configured

Windows + PowerShell

DEV_MODE=1

Start backend:

cd D:\StartUp\Licitra
.\.venv\Scripts\Activate.ps1
$env:DEV_MODE="1"
python -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000

Leave server running.

Reset organizations
Invoke-RestMethod -Method Post http://127.0.0.1:8000/dev/reset/org1
Invoke-RestMethod -Method Post http://127.0.0.1:8000/dev/reset/org2
Generate events

Org1 (20 events):

1..20 | % {
  $b=@{org_id="org1";event_id="e$_";payload=@{seq=$_;org="org1"}}|ConvertTo-Json -Compress
  Invoke-RestMethod -Method Post http://127.0.0.1:8000/events -ContentType "application/json" -Body $b
}

Org2 (10 events):

1..10 | % {
  $b=@{org_id="org2";event_id="e$_";payload=@{seq=$_;org="org2"}}|ConvertTo-Json -Compress
  Invoke-RestMethod -Method Post http://127.0.0.1:8000/events -ContentType "application/json" -Body $b
}
Verify pre-tamper
Invoke-RestMethod http://127.0.0.1:8000/verify/org1
Invoke-RestMethod http://127.0.0.1:8000/verify/org2

Expected:

Both return "ok": true.

Tamper org1
Invoke-RestMethod -Method Post http://127.0.0.1:8000/tamper/org1/e7
Verify post-tamper
Invoke-RestMethod http://127.0.0.1:8000/verify/org1
Invoke-RestMethod http://127.0.0.1:8000/verify/org2

Expected:

org1 → ok:false with bad_index

org2 → remains ok:true

This proves deterministic tamper detection + org isolation.

Export evidence

JSON:

Invoke-RestMethod http://127.0.0.1:8000/evidence/org1 | ConvertTo-Json -Depth 80 > evidence_org1_tampered.json
Invoke-RestMethod http://127.0.0.1:8000/evidence/org2 | ConvertTo-Json -Depth 80 > evidence_org2_ok.json

PDF:

Invoke-WebRequest http://127.0.0.1:8000/evidence/org1/pdf -OutFile evidence_org1_tampered.pdf
Invoke-WebRequest http://127.0.0.1:8000/evidence/org2/pdf -OutFile evidence_org2_ok.pdf

Artifacts appear in this folder.

Expected Results
Org1 (tampered)

evidence_org1_tampered.json

evidence_org1_tampered.pdf

Verification fails with bad_index.

Org2 (clean)

evidence_org2_ok.json

evidence_org2_ok.pdf

Verification remains ok:true.

Demonstrates multi-org isolation.

LICITRA provides cryptographic runtime integrity — not observability.