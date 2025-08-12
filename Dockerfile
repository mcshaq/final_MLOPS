FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY procfile.pkl .
COPY api.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"] 