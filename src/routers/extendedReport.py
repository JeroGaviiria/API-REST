from fastapi import APIRouter, Body, HTTPException, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.extendedReport import ExtendedReport  
from src.schemas.ingresos import Ingreso 
from src.schemas.egresos import Egreso    

extendedReport_router = APIRouter()
ingresos: List[Ingreso] = []
egresos: List[Egreso] = []

@extendedReport_router.get('/reporte-ampliado', tags=['reportes'], response_model=ExtendedReport, description="Generar reporte ampliado de gastos")
def generate_extended_report():
    ingresos_por_categoria = {}
    egresos_por_categoria = {}

    for ingreso in ingresos:
        ingresos_por_categoria[ingreso.categoria] = ingresos_por_categoria.get(ingreso.categoria, 0) + ingreso.valor
    
    for egreso in egresos:
        egresos_por_categoria[egreso.categoria] = egresos_por_categoria.get(egreso.categoria, 0) + egreso.valor
    
    return ExtendedReport(ingresos_por_categoria=ingresos_por_categoria, egresos_por_categoria=egresos_por_categoria)