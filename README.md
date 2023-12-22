# API_ECG
Crear entorno virtual
```bash
sudo apt install python3.10-venv
python3 -m venv .venv
source .venv/bin/activate
```

Install FastAPI and Uvicorn
```bash
pip install fastapi
pip install uvicorn
```

Run Uvicorn server
```bash
uvicorn main:app --reload
```