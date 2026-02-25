Demo notes:

* The runnable FastAPI demo lives in the private core repo.
* This repo contains the reference primitives and deterministic vectors.



\# LICITRA Demo Evidence (Multi-Org)



These artifacts prove LICITRA’s tamper-evident runtime ledger behavior.



\## What to look at



\### Org1 (tampered)

\- `evidence\_org1\_tampered.json`

\- `evidence\_org1\_tampered.pdf`



Expected:

\- Verification fails (`ok:false`)

\- `bad\_index` points to the first broken link (0-based indexing)

\- The chain tail no longer verifies



\### Org2 (clean / isolated)

\- `evidence\_org2\_ok.json`

\- `evidence\_org2\_ok.pdf`



Expected:

\- Verification remains `ok:true`

\- Demonstrates multi-org isolation (org1 corruption does not affect org2)



\## How these were generated



Backend:

\- `POST /dev/reset/{org}`

\- `POST /events` (event loop)

\- `POST /tamper/{org}/{event\_id}` (dev-only)

\- `GET /verify/{org}`

\- `GET /evidence/{org}`

\- `GET /evidence/{org}/pdf`

