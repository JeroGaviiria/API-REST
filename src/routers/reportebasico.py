from fastapi import APIRouter, HTTPException
from typing import List
from src.schemas.ingresos import Ingreso
from src.schemas.egresos import Egreso
from src.schemas.reportebasico import ReporteBasico

basicReport_router = APIRouter()

ingresos: List[Ingreso] = []
def get_ingresos():
    return ingresos

egresos: List[Egreso] = []
def get_egresos():
    return egresos

@basicReport_router.get("/reporte_basico", response_model=ReporteBasico)
async def obtener_reporte_basico():
    try:
        # Calcular total de ingresos
        total_ingresos = sum(ingreso.valor for ingreso in ingresos)
        
        # Calcular total de egresos
        total_egresos = sum(egreso.valor for egreso in egresos)
        
        # Calcular balance
        balance = total_ingresos - total_egresos
        
        return {"total_ingresos": total_ingresos, "total_egresos": total_egresos, "balance": balance}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al generar el reporte básico: {}".format(str(e)))
