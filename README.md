# Predictor de Precios de Casas en Boston

API para predecir precios de casas en Boston basado en el número de habitaciones y el porcentaje de población de bajo estatus. 

## Despliegue en Producción


### Usando la interfaz web:

1. Ve a https://casas-boston.fly.dev/docs
2. Haz clic en el endpoint POST `/prediccion/`
3. Haz clic en "Try it out"
4. Ingresa los valores en el JSON:
   ```json
   {
     "rooms": 6.0,
     "lower_status_pct": 15.0
   }
   ```
5. Haz clic en "Execute"

## Parámetros del Modelo

- **`rooms`**: Número promedio de habitaciones (entre 1 y 20)
- **`lower_status_pct`**: Porcentaje de población de bajo estatus (entre 0 y 100)

## Respuesta de la API

La API retorna un JSON con:
- **`precio_predicho`**: Precio estimado en miles de dólares
- **`unidad`**: Unidad de medida
- **`features_utilizadas`**: Valores usados para la predicción

## Desarrollo Local (Opcional)

Si quieres ejecutar la API localmente para desarrollo:

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecutar la API:
```bash
uvicorn api:app --reload
```

3. Visitar http://127.0.0.1:8000/docs para ver la documentación

## Estructura del Proyecto

```
.
├── api.py              # API FastAPI
├── procfile.pkl        # Modelo entrenado
├── requirements.txt    # Dependencias
├── Dockerfile         # Configuración para Docker
└── fly.toml           # Configuración para Fly.io
```

## Tecnologías Utilizadas

- **FastAPI**: Framework web para la API
- **scikit-learn**: Modelo de Machine Learning
- **Docker**: Para imagenes
- **Fly.io**: Plataforma de despliegue
- **Python 3.9**: Lenguaje de programación

## NOTA:
- Dataset alojado en http://lib.stat.cmu.edu/datasets/boston
