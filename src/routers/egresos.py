from fastapi import APIRouter, Body, HTTPException, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.schemas.egresos import Egreso


egresos_router = APIRouter()


egresos: List[Egreso] = []


@egresos_router.post('/egresos', tags=['egresos'], response_model=dict, description="Agregar un nuevo egreso")
def add_egreso(egreso: Egreso):
    egreso_dict = egreso.dict()
    egresos.append(egreso)
    return JSONResponse(content={"message": "El egreso se agregó correctamente", "data": egreso_dict}, status_code=201)

@egresos_router.get('/egresos', tags=['egresos'], response_model=List[Egreso], description="Listar todos los egresos")
def get_all_egresos():
    return egresos

@egresos_router.delete('/egresos/{egreso_id}', tags=['egresos'], response_model=dict, description="Eliminar un egreso específico")
def remove_egreso(egreso_id: int = Path(..., description="ID del egreso a eliminar")):
    egreso_index = next((index for index, egreso in enumerate(egresos) if egreso.id == egreso_id), None)
    if egreso_index is None:
        raise HTTPException(status_code=404, detail="Egreso no encontrado")
    removed_egreso = egresos.pop(egreso_index)
    return {"message": "El egreso se eliminó correctamente", "data": removed_egreso}