# Predictor de Precios de Casas en Boston

API para predecir precios de casas en Boston basado en el número de habitaciones y el porcentaje de población de bajo estatus.

## Estructura del Proyecto

```
.
├── api.py              # API FastAPI
├── procfile.pkl        # Modelo entrenado
├── requirements.txt    # Dependencias
├── Dockerfile         # Configuración para Docker
└── fly.toml           # Configuración para Fly.io
```

## Despliegue Local

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecutar la API:
```bash
uvicorn api:app --reload
```

3. Visitar http://127.0.0.1:8000/docs para ver la documentación y probar la API

## Despliegue en Fly.io

1. Instalar Fly CLI:
```bash
curl -L https://fly.io/install.sh | sh
```

2. Login en Fly.io:
```bash
fly auth login
```

3. Desplegar la aplicación:
```bash
fly launch
fly deploy
```

## Uso de la API

Hacer una predicción usando curl:

```bash
curl -X POST "https://tu-app.fly.dev/prediccion/" \
     -H "Content-Type: application/json" \
     -d '{"rooms": 6.0, "lower_status_pct": 15.0}'
```

O usando Python:

```python
import requests

url = "https://tu-app.fly.dev/prediccion/"
data = {
    "rooms": 6.0,
    "lower_status_pct": 15.0
}

response = requests.post(url, json=data)
print(response.json())
```

## Parámetros del Modelo

- `rooms`: Número promedio de habitaciones (entre 1 y 20)
- `lower_status_pct`: Porcentaje de población de bajo estatus (entre 0 y 100)

## Respuesta

La API retorna un JSON con:
- `precio_predicho`: Precio estimado en miles de dólares
- `unidad`: Unidad de medida
- `features_utilizadas`: Valores usados para la predicción 