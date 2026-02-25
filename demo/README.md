# LICITRA Demo — Runtime Integrity Walkthrough (Multi-Org)

This demo demonstrates LICITRA’s cryptographic runtime integrity guarantees:

- Deterministic SHA-256 hash chaining  
- Exact tamper detection with failure index  
- Multi-organization isolation  
- JSON + PDF forensic evidence export  

These artifacts prove LICITRA’s runtime integrity behavior.

---

## Prerequisites

- LICITRA core running locally  
- PostgreSQL configured  
- Windows + PowerShell  
- DEV_MODE=1  

---

## Start Backend

```powershell
cd D:\StartUp\Licitra
.\.venv\Scripts\Activate.ps1
$env:DEV_MODE="1"
python -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
```

Leave server running.

---

## Reset Organizations

Open a second PowerShell window:

```powershell
Invoke-RestMethod -Method Post http://127.0.0.1:8000/dev/reset/org1
Invoke-RestMethod -Method Post http://127.0.0.1:8000/dev/reset/org2
```

---

## Generate Events

### Org1 (20 events)

```powershell
1..20 | % {
  $b=@{org_id="org1";event_id="e$_";payload=@{seq=$_;org="org1"}} |
    ConvertTo-Json -Compress
  Invoke-RestMethod -Method Post http://127.0.0.1:8000/events `
    -ContentType "application/json" -Body $b
}
```

### Org2 (10 events)

```powershell
1..10 | % {
  $b=@{org_id="org2";event_id="e$_";payload=@{seq=$_;org="org2"}} |
    ConvertTo-Json -Compress
  Invoke-RestMethod -Method Post http://127.0.0.1:8000/events `
    -ContentType "application/json" -Body $b
}
```

---

## Verify Pre-Tamper

```powershell
Invoke-RestMethod http://127.0.0.1:8000/verify/org1
Invoke-RestMethod http://127.0.0.1:8000/verify/org2
```

Expected: both return `ok:true`.

---

## Tamper Org1

```powershell
Invoke-RestMethod -Method Post http://127.0.0.1:8000/tamper/org1/e7
```

---

## Verify Post-Tamper

```powershell
Invoke-RestMethod http://127.0.0.1:8000/verify/org1
Invoke-RestMethod http://127.0.0.1:8000/verify/org2
```

Expected:

- org1 → ok:false with bad_index  
- org2 → remains ok:true  

---

## Export Evidence

### JSON

```powershell
Invoke-RestMethod http://127.0.0.1:8000/evidence/org1 |
  ConvertTo-Json -Depth 80 > evidence_org1_tampered.json

Invoke-RestMethod http://127.0.0.1:8000/evidence/org2 |
  ConvertTo-Json -Depth 80 > evidence_org2_ok.json
```

### PDF

```powershell
Invoke-WebRequest http://127.0.0.1:8000/evidence/org1/pdf `
  -OutFile evidence_org1_tampered.pdf

Invoke-WebRequest http://127.0.0.1:8000/evidence/org2/pdf `
  -OutFile evidence_org2_ok.pdf
```

---

## Expected Results

Org1 (tampered):
- evidence_org1_tampered.json  
- evidence_org1_tampered.pdf  

Org2 (clean):
- evidence_org2_ok.json  
- evidence_org2_ok.pdf  

---

## Summary

LICITRA provides cryptographic runtime integrity — not observability.

Every AI interaction becomes a chained, verifiable event.

Any historical modification breaks the chain and is detected immediately.

This is forensic-grade runtime governance for agentic systems.
