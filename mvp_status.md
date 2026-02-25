# MVP Status

## Implemented

- FastAPI backend  
- PostgreSQL persistence  
- Per-organization hash-chained ledger  
- Deterministic canonical JSON hashing  
- Replay protection (409 on duplicate events)  
- Verification endpoint  
- Payload tamper detection  
- Previous-hash tamper detection  
- Deletion detection  
- Multi-organization isolation  
- Evidence bundle export (JSON)  
- Governance PDF export  
- DEV_MODE gated attack endpoints  
- Rollback v0 decision primitive  

---

## Not Implemented

- Authentication / API keys  
- UI dashboards  
- Streaming ingestion  
- Real-time alerts  
- Cloud deployment  

---

This MVP intentionally focuses on cryptographic runtime integrity primitives only.

Everything else (auth, UI, deployment) is deferred until core correctness and evidence generation are validated.
