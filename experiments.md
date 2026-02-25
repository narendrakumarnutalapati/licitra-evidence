\# LICITRA Experiments



This document records reproducible integrity and tamper-detection experiments.



\## Experiment 1 — Clean Chain (100 Events)



\- org1 reset

\- 100 sequential events ingested

\- verify(org1) => ok=true, count=100



Artifact:

demo/evidence\_org1\_100\_ok.json



Result:

Deterministic hash chain persisted to PostgreSQL and verified.



---



\## Experiment 2 — Payload Tamper (Mid-chain)



\- org1 event e50 payload modified directly in DB

\- verify(org1) => ok=false, bad\_index=49, reason=hash\_mismatch



Artifact:

demo/evidence\_org1\_tamper\_payload\_e50.json



Result:

System detects payload mutation inside chain.



---



\## Experiment 3 — Prev-hash Tamper



\- org1 event e10 prev\_hash overwritten

\- verify(org1) => ok=false, bad\_index=9, reason=prev\_hash\_mismatch



Artifact:

demo/evidence\_org1\_tamper\_prev\_e10.json



Result:

System detects chain re-linking / reordering.



---



\## Experiment 4 — Multi-org Isolation



\- org1: 100 events

\- org2: 50 events

\- org1 tampered at e50

\- verify(org1) => fail

\- verify(org2) => ok



Artifacts:

demo/evidence\_multi\_org\_org1\_tampered.json  

demo/evidence\_multi\_org\_org2\_ok.json



Result:

Tampering one organization does not affect others.

