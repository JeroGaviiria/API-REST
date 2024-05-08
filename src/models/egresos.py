from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from src.config.database import Base


class Egreso(Base):
    __tablename__ = 'egresos'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fecha = Column(String)
    descripcion = Column(String, index=True)
    valor = Column(Float)
    categoria = Column(String)
