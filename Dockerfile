FROM python:3.9-slim

WORKDIR /app

# Crear el directorio code_final
RUN mkdir code_final

# Copiar los archivos manteniendo la estructura
COPY requirements.txt .
COPY procfile.pkl code_final/
COPY api.py code_final/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "code_final.api:app", "--host", "0.0.0.0", "--port", "8080"] 