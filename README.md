# LICITRA Evidence Repository

Cryptographically Verifiable Runtime Integrity for Agentic AI Systems.

This repository contains reproducible experiments, exported evidence bundles, and supporting documentation for LICITRA.

---

## Quick Start (5 Minutes)

1. Run LICITRA core locally (see docs/how_to_run.md)
2. Follow the demo walkthrough in `demo/README.md`
3. Inspect generated JSON + PDF evidence artifacts

ðŸ‘‰ Start here: `demo/README.md`

---

## Whatâ€™s Included

- `docs/` - threat model, scope, and experiment methodology  
- `demo/` - reproducible demo walkthrough + exported evidence bundles (JSON/PDF)  
- `docs/experiments.md` - step-by-step commands to reproduce tamper detection tests  
- `docs/proof.md` - summary of results and what each artifact demonstrates  
- `docs/how_to_run.md` - instructions to run the system locally  

---

## Evidence Summary

Included demo artifacts demonstrate:

- org1: intentional tampering detected at `bad_index`
- org2: remains clean (multi-organization isolation)
- JSON + PDF forensic exports
- Deterministic SHA-256 hash-chain verification

Artifacts:

- `demo/evidence_org1_tampered.json`
- `demo/evidence_org1_tampered.pdf`
- `demo/evidence_org2_ok.json`
- `demo/evidence_org2_ok.pdf`

---

## Key Claims Demonstrated

- Hash-chained semantic event integrity (tamper detection)
- Multi-organization isolation (org1 chain independent from org2)
- Detection of record mutation, deletion, and previous-hash corruption
- Evidence bundles suitable for governance / audit workflows

---

## Architecture

Core implementation lives here:

https://github.com/narendrakumarnutalapati/licitra-core

The core repository contains:

- FastAPI backend
- PostgreSQL ledger implementation
- Deterministic SHA-256 chaining
- Tamper simulation endpoints
- Evidence export (JSON + PDF)

---

## Version

Evidence Bundle Version: 0.1-evidence

---

LICITRA provides cryptographic runtime integrity - not observability.

Every AI interaction becomes a chained, verifiable event.

Any historical modification breaks the chain and is detected immediately.

This is forensic-grade runtime governance for agentic AI systems.
