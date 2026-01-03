from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.schemas import DensityInput, PlantingSystem
import math

app = FastAPI(
    title="Agro-Solver API",
    description="Backend API for Agro-Solver platform",
    version="0.1.0"
)

# TODO: SEGURIDAD - Restringir orígenes antes de producción
# Actualmente se permite '*' para facilitar el desarrollo local.
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
    Root endpoint to verify API availability.
    """
    return {"message": "Agro-Solver API is running", "version": "0.2.0"}

@app.post("/api/density")
def calculate_density(data: DensityInput):
    """
    Calculate planting density based on distances and system.
    """
    try:
        # Standard Formula: 10000 / (d1 * d2)
        base_density = 10000 / (data.row_distance * data.plant_distance)
        
        # Apply Efficiency Factor for Triangular (Tresbolillo)
        # Factor is 1 / sin(60°) ≈ 1.1547 (which means dividing by 0.866 in the denominator)
        if data.system == PlantingSystem.TRIANGULAR:
            # Formula: 10000 / (d1 * d2 * 0.866025)
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
