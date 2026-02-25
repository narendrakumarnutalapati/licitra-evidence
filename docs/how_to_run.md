# How to Run LICITRA Locally

## Requirements

- Python 3.12+
- PostgreSQL 16
- Windows PowerShell
- Git

---

## Setup

```powershell
git clone https://github.com/narendrakumarnutalapati/licitra-core.git
cd licitra-core

python -m venv .venv
.\.venv\Scripts\Activate.ps1

pip install -r backend/requirements.txt
```

Create environment variables:

```powershell
$env:DATABASE_URL="postgresql+psycopg://licitra_user:licitra_pass@localhost:5432/licitra"
$env:DEV_MODE="1"
```

Run server:

```powershell
python -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
```

Server runs at:

http://127.0.0.1:8000

---

## Core Endpoints

- POST /events  
- GET /verify/{org_id}  
- GET /evidence/{org_id}  
- GET /evidence/{org_id}/pdf  

---

## Development Only Endpoints

- POST /dev/reset/{org_id}  
- POST /tamper/{org_id}/{event_id}  
- POST /tamper-prev/{org_id}/{event_id}  
- POST /dev/delete/{org_id}/{event_id}  

DEV endpoints require DEV_MODE=1.

---

LICITRA implements a cryptographically chained runtime ledger for agentic AI systems.

Each event is canonically serialized, SHA-256 hashed, and linked to the previous event.

Any historical modification invalidates the chain and is detected during verification.
