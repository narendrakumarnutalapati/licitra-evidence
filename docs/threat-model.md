## Threat Model (MVP)

Threats:
1) Log tampering (mutate stored payloads)
2) Replay / reordering of events
3) Partial log deletion
4) Forged events without valid chain context

Controls (MVP):
- Hash chain with prev_hash anchoring per organization
- Deterministic canonical JSON hashing to prevent serialization ambiguity
- Verification routine that detects tampering/reorder

Non-goals (MVP):
- Confidentiality / encryption at rest
- AuthN/AuthZ, multi-tenant isolation hardening
- Hardware root of trust
