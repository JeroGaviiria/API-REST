from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from src.config.database import Base

class Ingreso(Base):
    __tablename__ = 'ingresos'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fecha = Column(String)
    descripcion = Column(String, index=True)
    valor = Column(Float)
    categoria = Column(String)