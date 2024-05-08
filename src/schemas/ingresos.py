from typing import List, Optional
from pydantic import BaseModel, Field, validator, model_validator


class Ingreso(BaseModel):
    id: int = Field(default_factory=lambda: len(ingresos) + 1, title="ID del ingreso")
    fecha: str = Field(..., title="Fecha del ingreso en formato YYYY-MM-DD")
    descripcion: str = Field(..., title="Descripción del ingreso")
    valor: float = Field(default=0, ge=0, title="Valor del ingreso")
    categoria: str = Field(..., title="Categoría del ingreso")

    @validator("valor")
    def validate_valor(cls, v):
        if v < 0:
            raise ValueError("El valor del ingreso no puede ser negativo")
        return v

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "fecha": "2024-02-11",
                "descripcion": "Sueldo",
                "valor": 1200000,
                "categoria": "Trabajo"
            }
        }

ingresos: List[Ingreso] = []