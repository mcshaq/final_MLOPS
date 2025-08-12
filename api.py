from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pickle
import numpy as np

# Cargar el modelo desde el archivo .pkl
with open('procfile.pkl', 'rb') as archivo_modelo:
    modelo = pickle.load(archivo_modelo)

# Crear la aplicación FastAPI
app = FastAPI(
    title="Predicción de Precios de Casas en Boston",
    description="API para predecir precios de casas basado en el número de habitaciones y el porcentaje de población de bajo estatus",
    version="1.0.0"
)

# Definir el modelo de datos de entrada utilizando Pydantic
class Casa(BaseModel):
    rooms: float = Field(
        ..., 
        description="Número promedio de habitaciones",
        ge=1,
        le=20,
        example=6.0
    )
    lower_status_pct: float = Field(
        ..., 
        description="Porcentaje de población de bajo estatus",
        ge=0,
        le=100,
        example=15.0
    )

# Definir el modelo de datos de salida
class Prediccion(BaseModel):
    precio_predicho: float
    unidad: str
    features_utilizadas: dict

@app.post("/prediccion/", 
    response_model=Prediccion,
    summary="Predecir precio de casa",
    description="Predice el precio de una casa en Boston basado en el número de habitaciones y el porcentaje de población de bajo estatus"
)
async def predecir_precio(casa: Casa):
    """
    Realiza una predicción del precio de una casa basado en:
    - **rooms**: Número promedio de habitaciones (entre 1 y 20)
    - **lower_status_pct**: Porcentaje de población de bajo estatus (entre 0 y 100)
    
    Retorna:
    - Precio predicho en miles de dólares
    - Unidad de medida
    - Features utilizadas en la predicción
    """
    try:
        # Preparar los datos de entrada
        features = np.array([[casa.rooms, casa.lower_status_pct]])
        
        # Realizar la predicción
        precio_predicho = modelo.predict(features)[0]
        
        # Construir la respuesta
        resultado = {
            "precio_predicho": float(precio_predicho),
            "unidad": "miles de dólares",
            "features_utilizadas": {
                "rooms": casa.rooms,
                "lower_status_pct": casa.lower_status_pct
            }
        }
        
        return resultado
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 