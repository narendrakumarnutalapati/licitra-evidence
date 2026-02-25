# Cryptographic Proof Summary

LICITRA implements an append-only cryptographic hash chain per organization:

```
current_hash = SHA256(prev_hash || canonical_json(payload))
```

Each organization maintains an independent ledger.

Verification recomputes the full chain from GENESIS and validates every link.

---

## Tampering Scenarios Detected

- Payload mutation  
- Previous-hash overwrite  
- Deletion or reordering of events  
- Replay attacks (duplicate event_id)  

---

## Evidence Bundles Include

- Verification report  
- Full ordered event chain  
- Rollback decision (when integrity fails)  
- Timestamp  
- SHA-256 bundle checksum  

---

## PDF Exports Include

- Organization ID  
- Verification status  
- Event count  
- First and last hashes  
- Tail chain link proof  
- Embedded JSON evidence  
- Bundle checksum  

---

## Reproducibility

All experiments are fully reproducible using PowerShell scripts in this repository.

Artifacts in the `demo/` directory correspond directly to experiments documented in `experiments.md`.

---

LICITRA converts runtime behavior into cryptographically verifiable evidence.

Any historical modification invalidates the chain and is detected deterministically.
