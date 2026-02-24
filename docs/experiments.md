## Validation Experiments (MVP)

1) Tamper test:
- Ingest event e1, verify OK
- Mutate payload of e1, verify FAIL with hash_mismatch

2) Replay test:
- Ingest e1 then e2
- Attempt to insert replayed e1 or reorder events (in DB version)
- Verify FAIL with prev_hash_mismatch

Outputs:
- JSON evidence bundles containing event chain + verification report
- Reproducible test vectors for canonical JSON hashing
