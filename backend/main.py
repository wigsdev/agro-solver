from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.schemas import DensityInput, PlantingSystem

app = FastAPI(
    title="Agro-Solver API",
    description="API Backend para la plataforma Agro-Solver",
    version="0.2.0"
)

# Configuración CORS
# Permite solicitudes de cualquier origen (útil para desarrollo y producción simple)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """
    Endpoint raíz para verificar la disponibilidad de la API.
    """
    return {"message": "Agro-Solver API is running", "version": "0.2.0"}

@app.post("/api/density")
def calculate_density(data: DensityInput):
    """
    Calcula la densidad de siembra basada en las distancias y el sistema.
    """
    try:
        # Fórmula Estándar: 10000 / (d1 * d2)
        base_density = 10000 / (data.row_distance * data.plant_distance)
        
        # Aplicar Factor de Eficiencia para Tresbolillo (Triangular)
        # El factor es 1 / sin(60°) ≈ 1.1547 (lo que significa dividir por 0.866 en el denominador)
        if data.system == PlantingSystem.TRIANGULAR:
            # Fórmula: 10000 / (d1 * d2 * 0.866025)
            plants_per_hectare = base_density / 0.8660254
        else:
            plants_per_hectare = base_density

        return {
            "plants_per_hectare": round(plants_per_hectare),
            "row_distance_used": data.row_distance,
            "plant_distance_used": data.plant_distance,
            "system_used": data.system
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
