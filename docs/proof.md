## Proof (60 seconds)

Core properties:
- Deterministic canonical JSON hashing
- Hash-chained audit ledger with prev_hash anchoring
- Verification detects tamper

Suggested demo steps (core repo):
1) POST /events for org1:e1
2) GET /verify/org1 => ok:true
3) POST /tamper/org1/e1
4) GET /verify/org1 => ok:false, reason:hash_mismatch
