\# How to Run LICITRA Locally



\## Requirements



\- Python 3.12+

\- PostgreSQL 16

\- Windows PowerShell

\- Git



---



\## Setup



```powershell

git clone https://github.com/narendrakumarnutalapati/licitra-core.git

cd licitra-core

python -m venv .venv

.\\.venv\\Scripts\\Activate.ps1

pip install -r backend/requirements.txt



Create environment:



$env:DATABASE\_URL="postgresql+psycopg://licitra\_user:licitra\_pass@localhost:5432/licitra"

$env:DEV\_MODE="1"



Run server:



python -m uvicorn backend.app.main:app



Server runs at:



http://127.0.0.1:8000



Core Endpoints



POST /events

GET /verify/{org\_id}

GET /evidence/{org\_id}

GET /evidence/{org\_id}/pdf



DEV ONLY:



POST /dev/reset/{org\_id}

POST /tamper/{org\_id}/{event\_id}

POST /tamper-prev/{org\_id}/{event\_id}

POST /dev/delete/{org\_id}/{event\_id}



DEV endpoints require DEV\_MODE=1.

