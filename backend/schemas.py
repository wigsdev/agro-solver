from enum import Enum
from pydantic import BaseModel, Field

class PlantingSystem(str, Enum):
    SQUARE = "square"
    TRIANGULAR = "triangular"

class DensityInput(BaseModel):
    row_distance: float = Field(..., gt=0, description="Distance between rows in meters")
    plant_distance: float = Field(..., gt=0, description="Distance between plants in meters")
    system: PlantingSystem = Field(
        default=PlantingSystem.SQUARE, 
        description="Planting arrangement system: 'square' (rect) or 'triangular' (tresbolillo)"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "row_distance": 2.0,
                "plant_distance": 2.0,
                "system": "square"
            }
        }
