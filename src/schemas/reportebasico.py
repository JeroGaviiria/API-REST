from pydantic import BaseModel

class ReporteBasico(BaseModel):
    total_ingresos: float
    total_egresos: float
    balance: float
