from fastapi import FastAPI
from src.middlewares.error_handler import ErrorHandler
from src.routers.ingresos import ingresos_router
from src.routers.egresos import egresos_router
from src.routers.reportebasico import basicReport_router
from src.routers.extendedReport import extendedReport_router
from src.config.database import Base, engine
from src.models.ingresos import Ingreso
from src.models.egresos import Egreso

app = FastAPI()
Base.metadata.create_all(bind=engine)

<<<<<<< HEAD
app.add_middleware(ErrorHandler)

app.include_router(prefix="/ingresos", router=ingresos_router)
app.include_router(prefix="/egresos", router=egresos_router)
app.include_router(prefix="/generate_basic_report", router=basicReport_router)
app.include_router(prefix="/reporte-ampliado", router=extendedReport_router)

Base.metadata.create_all(bind=engine)
=======

class Usuario(BaseModel):
    ingresos: List[Dict] = []
    egresos: List[Dict] = []


usuario = Usuario()


ingreso_id_counter = 0
egreso_id_counter = 0


class TransaccionBase(BaseModel):
    fecha: str
    descripcion: str
    valor: float
    categoria: str

class Ingreso(TransaccionBase):
    id: int = None

class Egreso(TransaccionBase):
    id: int = None


@app.post("/ingresos/")
def agregar_ingreso(ingreso: Ingreso):
    global ingreso_id_counter
    ingreso_id_counter += 1
    ingreso.id = ingreso_id_counter
    usuario.ingresos.append(ingreso.dict())
    return JSONResponse(content={"message": "Ingreso agregado exitosamente", "id": ingreso.id})

@app.post("/egresos/")
def agregar_egreso(egreso: Egreso):
    global egreso_id_counter
    egreso_id_counter += 1
    egreso.id = egreso_id_counter
    usuario.egresos.append(egreso.dict())
    return JSONResponse(content={"message": "Egreso agregado exitosamente", "id": egreso.id})

@app.get("/ingresos/")
def listar_ingresos() -> List[Dict]:
    return usuario.ingresos

@app.get("/egresos/")
def listar_egresos() -> List[Dict]:
    return usuario.egresos


@app.get("/reporte_basico/")
def generar_reporte_basico():
    total_ingresos = sum(ingreso["valor"] for ingreso in usuario.ingresos)
    total_egresos = sum(egreso["valor"] for egreso in usuario.egresos)
    balance_actual = total_ingresos - total_egresos
    return JSONResponse(content={
        "total_ingresos": total_ingresos,
        "total_egresos": total_egresos,
        "balance_actual": balance_actual
    })

@app.get("/reporte_ampliado/")
def generar_reporte_ampliado():
    ingresos_por_categoria = {}
    egresos_por_categoria = {}
    
    for ingreso in usuario.ingresos:
        categoria = ingreso["categoria"]
        ingresos_por_categoria[categoria] = ingresos_por_categoria.get(categoria, 0) + ingreso["valor"]
    
    for egreso in usuario.egresos:
        categoria = egreso["categoria"]
        egresos_por_categoria[categoria] = egresos_por_categoria.get(categoria, 0) + egreso["valor"]
    
    return JSONResponse(content={
        "ingresos_por_categoria": ingresos_por_categoria,
        "egresos_por_categoria": egresos_por_categoria
    })


@app.delete("/eliminar_ingreso/{id}")
def eliminar_ingreso(id: int):
    for i, ingreso in enumerate(usuario.ingresos):
        if ingreso["id"] == id:
            del usuario.ingresos[i]
            return JSONResponse(content={"message": "Ingreso eliminado exitosamente"})
    raise HTTPException(status_code=404, detail="No se encontró el ingreso con el ID proporcionado")

@app.delete("/eliminar_egreso/{id}")
def eliminar_egreso(id: int):
    for i, egreso in enumerate(usuario.egresos):
        if egreso["id"] == id:
            del usuario.egresos[i]
            return JSONResponse(content={"message": "Egreso eliminado exitosamente"})
    raise HTTPException(status_code=404, detail="No se encontró el egreso con el ID proporcionado")
>>>>>>> dc12d39dfef51e31b5af688b1caa385ec1407ead
