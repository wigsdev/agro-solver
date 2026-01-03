from enum import Enum
from pydantic import BaseModel, Field

class PlantingSystem(str, Enum):
    SQUARE = "square"
    TRIANGULAR = "triangular"

class DensityInput(BaseModel):
    row_distance: float = Field(..., gt=0, description="Distancia entre surcos en metros")
    plant_distance: float = Field(..., gt=0, description="Distancia entre plantas en metros")
    system: PlantingSystem = Field(
        default=PlantingSystem.SQUARE, 
        description="Sistema de siembra: 'square' (cuadro/rectángulo) o 'triangular' (tresbolillo)"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "row_distance": 2.0,
                "plant_distance": 2.0,
                "system": "square"
            }
        }
