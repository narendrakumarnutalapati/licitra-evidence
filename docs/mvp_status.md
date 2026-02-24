\# LICITRA MVP Status (as of Feb 2026)



\## Summary



LICITRA is an experimental runtime governance primitive for agentic AI systems.



The MVP implements:



\- Deterministic canonical JSON hashing

\- Per-organization SHA-256 hash–chained audit ledger

\- Runtime verification endpoint (detects tampering and reorder)

\- Minimal Node SDK for event capture

\- Rollback v0 circuit-breaker decision record

\- JSON evidence bundle export for governance workflows



This establishes cryptographic runtime integrity as a technical primitive.



The current system is implemented using FastAPI (Python) with an in-memory ledger for MVP validation. Persistence is planned via PostgreSQL.



---



\## Architecture (MVP)



Agent / Application  

→ LICITRA Node SDK  

→ FastAPI Backend  

→ Hash-Chained Ledger  

→ Verification Engine  

→ Rollback v0 Decision  

→ Evidence Bundle Export (JSON)



Each event includes:



\- org\_id

\- event\_id

\- prev\_hash

\- payload



The current\_hash is computed as:



SHA256(canonical\_json({org\_id, event\_id, prev\_hash, payload}))



This forms an immutable chain per organization.



---



\## Core Capabilities



\### 1. Deterministic Canonical JSON



All payloads are serialized with:



\- Sorted keys

\- No whitespace

\- UTF-8 encoding



This prevents hash ambiguity across runtimes.



---



\### 2. Hash-Chained Audit Ledger



Events are appended per organization with prev\_hash anchoring.



Any mutation or reordering breaks the chain.



---



\### 3. Verification



Endpoint:



GET /verify/{org\_id}



Returns:



\- ok: true if chain intact

\- ok: false with bad\_index and reason if tampered



---



\### 4. Tamper Detection (Experiment)



A dev-only endpoint mutates stored payloads to simulate compromise.



Verification reliably detects:



\- hash\_mismatch

\- prev\_hash\_mismatch



---



\### 5. Rollback v0



When verification fails, the system emits a rollback decision record:



\- org\_id

\- action: ROLLBACK\_V0

\- reason

\- restore\_to\_hash



This represents the control plane hook for restoring agent state.



---



\### 6. Evidence Bundle Export



Endpoint:



GET /evidence/{org\_id}



Returns a portable JSON artifact:



\- org\_id

\- timestamp (UTC)

\- verify\_report

\- rollback decision (if applicable)

\- format\_version



These bundles are suitable for:



\- governance review

\- incident reporting

\- third-party audit workflows



---



\## Validation Experiments (Completed)



\### Experiment A: Clean Chain



1\. Ingest two events

2\. Verify chain



Result:

\- ok: true

\- count: 2



Evidence bundle exported.



---



\### Experiment B: Tamper Detection



1\. Mutate payload of first event

2\. Verify chain



Result:

\- ok: false

\- reason: hash\_mismatch

\- bad\_index: 0



Incident evidence bundle exported including rollback decision.



---



\## Current Limitations (Intentional MVP Scope)



\- Ledger is in-memory (PostgreSQL integration pending)

\- Rollback v0 emits decision only (no live memory restore)

\- No authentication or tenant isolation

\- No encryption at rest

\- Single-process demo mode



These are planned for subsequent milestones.



---



\## Next Milestones



1\. PostgreSQL-backed ledger

2\. Durable verification across restarts

3\. Replay / reorder experiments at DB layer

4\. Evidence export to PDF

5\. Agent memory restoration hooks



---



\## Artifacts Produced



\- Hash-chained audit backend (FastAPI)

\- Deterministic JSON test vectors

\- Node SDK

\- Evidence bundles:

&nbsp; - evidence\_org1\_ok.json

&nbsp; - evidence\_org1\_tampered.json

\- Git commit history establishing authorship

