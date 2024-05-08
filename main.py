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

app.add_middleware(ErrorHandler)

app.include_router(prefix="/ingresos", router=ingresos_router)
app.include_router(prefix="/egresos", router=egresos_router)
app.include_router(prefix="/generate_basic_report", router=basicReport_router)
app.include_router(prefix="/reporte-ampliado", router=extendedReport_router)

Base.metadata.create_all(bind=engine)
