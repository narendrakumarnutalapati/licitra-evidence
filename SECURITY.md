# Security Policy

## Overview

The LICITRA Evidence Repository contains:

- Reproducible experiment artifacts
- JSON evidence bundles
- PDF audit reports
- Deterministic test vectors
- Documentation supporting the linear hash-chain runtime integrity model

This repository does **not** execute production services.
It is an artifact and reproducibility repository supporting LICITRA Core (hash-chain version).

---

## Supported Versions

| Version | Supported |
|---------|-----------|
| main    | ✅ Yes     |
| historical tags | ⚠️ Archive only |

Only the `main` branch reflects the latest verified experiment artifacts.

---

## Integrity Model (Hash-Chain)

LICITRA (hash-chain version) implements:

current_hash = SHA256(prev_hash || canonical_json(payload))

Each organization maintains an independent append-only chain.

The evidence artifacts included in this repository demonstrate:

- Detection of payload mutation
- Detection of previous-hash corruption
- Detection of deletion / reordering
- Multi-organization isolation
- Deterministic verification output

---

## What This Repository Guarantees

- Artifacts reflect exported output from LICITRA Core.
- Experiments are reproducible via documented PowerShell scripts.
- Verification results are deterministic when re-run locally.
- Evidence bundles include chain verification status and failure index (if applicable).

---

## What This Repository Does NOT Guarantee

- It does not prevent artifact deletion.
- It does not prevent GitHub commit history rewrite.
- It does not cryptographically sign commits.
- It does not act as a public anchoring mechanism.
- It does not secure production environments.

This repository demonstrates integrity behavior — it does not enforce it.

---

## Threat Model

### In Scope

- Silent mutation of committed event payloads
- Hash-chain corruption
- Event reordering or deletion
- Cross-organization contamination attempts

### Out of Scope

- Full database file deletion
- Root-level OS compromise
- Infrastructure takeover
- SHA-256 cryptographic breaks
- GitHub platform compromise

The integrity guarantees are enforced by LICITRA Core, not this repository.

---

## Reporting Issues

If you discover:

- Documentation inaccuracies
- Non-reproducible experiments
- Evidence bundle inconsistencies

Open a GitHub Issue in this repository.

For runtime vulnerabilities, refer to `SECURITY.md` in the licitra-core repository.

Alternatively contact:

narendrakumar.nutalapati@gmail.com

---

## Independent Verification Guidance

To independently verify artifacts:

1. Run LICITRA Core locally.
2. Reproduce the documented experiment.
3. Export JSON evidence.
4. Compare:
   - final chain hash
   - event count
   - verification status
   - bad_index (if tampered)

The evidence repository exists to demonstrate reproducibility and transparency.

---

## Transparency Statement

LICITRA is a cryptographic runtime integrity primitive.

This repository documents experimental outputs and verification artifacts for the linear hash-chain implementation.

All enforcement logic resides in LICITRA Core.
