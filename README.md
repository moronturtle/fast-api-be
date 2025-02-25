# A FastAPI backend Project with GraphQL, PostgreSQL, Redis, and Kafka
## installation and Run
- install Dev Containers
- docker-compose up --build
- Ctrl + Shift + P or Cmd + Shift + P on Mac
- Dev Containers: Attach to Running Container

## optional not using docker
- python -m venv venv
- Mac/Linux : source venv/bin/activate or Windows (PowerShell): venv\Scripts\activate
- pip install -r requirements.txt
- uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload