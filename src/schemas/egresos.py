from pydantic import BaseModel, Field, validator
from typing import List, Union


class Egreso(BaseModel):
    id: int = Field(default_factory=lambda: len(egresos) + 1, title="ID del egreso")
    fecha: str = Field(..., title="Fecha del egreso en formato YYYY-MM-DD")
    descripcion: str = Field(..., title="Descripción del egreso")
    valor: float = Field(default=0, ge=0, title="Valor del egreso")
    categoria: str = Field(..., title="Categoría del egreso")

    @validator("valor")
    def validate_valor(cls, v):
        if v < 0:
            raise ValueError("El valor del egreso no puede ser negativo")
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "fecha": "2024-02-10",
                "descripcion": "Cuota del Banco",
                "valor": 300000,
                "categoria": "Prestamo"
            }
        }


egresos: List[Egreso] = []


