\# LICITRA MVP – How to Run



\## Requirements



\- Windows

\- Python 3.10+

\- Git



---



\## Setup



```powershell

cd D:\\StartUp\\Licitra

py -m venv .venv

.\\.venv\\Scripts\\Activate.ps1

pip install -r backend\\requirements.txt



Run Server

python -m uvicorn backend.app.main:app --reload



Server runs at:



http://127.0.0.1:8000



Demo Sequence

Reset Org

Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/dev/reset/org1"

Ingest Events

Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/events" -ContentType "application/json" -Body '{"org\_id":"org1","event\_id":"e1","payload":{"intent":"search","action":"query","model":"gpt"}}'



Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/events" -ContentType "application/json" -Body '{"org\_id":"org1","event\_id":"e2","payload":{"intent":"summarize","action":"compress","model":"gpt"}}'

Verify Chain

Invoke-RestMethod -Uri "http://127.0.0.1:8000/verify/org1"



Expected:



ok: true



count: 2



Export Evidence Bundle (Clean)

Invoke-RestMethod -Uri "http://127.0.0.1:8000/evidence/org1" |

&nbsp; ConvertTo-Json -Depth 10 |

&nbsp; Out-File -Encoding utf8 evidence\_org1\_ok.json

Tamper Experiment

Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/tamper/org1/e1"

Verify Failure

Invoke-RestMethod -Uri "http://127.0.0.1:8000/verify/org1"



Expected:



ok: false



reason: hash\_mismatch



Export Incident Evidence

Invoke-RestMethod -Uri "http://127.0.0.1:8000/evidence/org1" |

&nbsp; ConvertTo-Json -Depth 10 |

&nbsp; Out-File -Encoding utf8 evidence\_org1\_tampered.json



These two JSON files represent:



normal operation



compromised runtime



They are suitable for governance or audit review.





---



\## Final step



Add these two files to `licitra-evidence/docs`, commit, and push:



```powershell

cd D:\\StartUp\\licitra-evidence

git add docs

git commit -m "Add MVP status and reproducible run instructions"

git push

