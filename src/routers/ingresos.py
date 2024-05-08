from pathlib import Path
from fastapi import APIRouter, Body, HTTPException
from typing import List
from src.schemas.ingresos import Ingreso
from src.models.ingresos import Ingreso as IngresoModel
from src.config.database import SessionLocal
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

ingresos_router = APIRouter()

@ingresos_router.post('/ingresos', tags=['ingresos'], response_model=dict, description="Crea un nuevo ingreso")
def create_ingreso(ingreso: Ingreso = Body(...)):
    db = SessionLocal()
    nuevo_ingreso = IngresoModel(**ingreso.dict())
    db.add(nuevo_ingreso)
    db.commit()
    db.refresh(nuevo_ingreso)
    db.close()
    return JSONResponse(content={"message": "El ingreso se creó correctamente", "data": ingreso.model_dump()}, status_code=201)

@ingresos_router.get('/ingresos/{id}', tags=['ingresos'], response_model=Ingreso, description="Devuelve los datos de un ingreso específico")
def get_ingreso(id: int = Path(..., ge=1, le=5000)):
    db = SessionLocal()
    ingreso = db.query(IngresoModel).filter(IngresoModel.id == id).first()
    db.close()
    if not ingreso:
        raise HTTPException(status_code=404, detail="Ingreso no encontrado")
    return ingreso

@ingresos_router.delete('/ingresos/{ingreso_id}', tags=['ingresos'], response_model=dict, description="Eliminar un ingreso específico")
def remove_ingreso(ingreso_id: int):
    db = SessionLocal()
    ingreso_db = db.query(IngresoModel).filter(IngresoModel.id == ingreso_id).first()
    if not ingreso_db:
        raise HTTPException(status_code=404, detail="Ingreso no encontrado")
    db.delete(ingreso_db)
    db.commit()
    db.close()
    return {"message": "El ingreso se eliminó correctamente", "data": ingreso_db}
