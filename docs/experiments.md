# LICITRA Experiments

This document records reproducible integrity and tamper-detection experiments.

---

## Experiment 1 — Clean Chain (100 Events)

- org1 reset  
- 100 sequential events ingested  
- verify(org1) => ok=true, count=100  

Artifact:

demo/evidence_org1_100_ok.json

Result:

Deterministic hash chain persisted to PostgreSQL and verified.

---

## Experiment 2 — Payload Tamper (Mid-chain)

- org1 event e50 payload modified directly in DB  
- verify(org1) => ok=false, bad_index=49, reason=hash_mismatch  

Artifact:

demo/evidence_org1_tamper_payload_e50.json

Result:

System detects payload mutation inside chain.

---

## Experiment 3 — Prev-hash Tamper

- org1 event e10 prev_hash overwritten  
- verify(org1) => ok=false, bad_index=9, reason=prev_hash_mismatch  

Artifact:

demo/evidence_org1_tamper_prev_e10.json

Result:

System detects chain re-linking / reordering.

---

## Experiment 4 — Multi-org Isolation

- org1: 100 events  
- org2: 50 events  
- org1 tampered at e50  
- verify(org1) => fail  
- verify(org2) => ok  

Artifacts:

demo/evidence_multi_org_org1_tampered.json  
demo/evidence_multi_org_org2_ok.json  


Result:

Tampering one organization does not affect others.

## Experiment 5 — 3-org variable scale (50/100/150) + PDF

Run ID: <paste runId from script output>

- orgA: 50 events (clean witness)
- orgB: 100 events (clean, exported)
- orgC: 150 events (tampered at e37, exported)
- Expected: orgC verify fails with bad_index=36, orgA+orgB remain ok:true
- Artifacts: demo/evidence_orgB_<runId>_ok.(json|pdf), demo/evidence_orgC_<runId>_tampered.(json|pdf), demo/summary_3org_big_<runId>.txt

---

Summary:

These experiments demonstrate deterministic hash chaining, payload integrity, previous-hash protection, and strict organizational isolation.

LICITRA converts runtime behavior into cryptographically verifiable evidence.
