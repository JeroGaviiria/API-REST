from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.config.database import Base

class ExtendedReport(Base):
    __tablename__ = 'extended_reports'

    
    ingresos_por_categoria = Column(String)
    egresos_por_categoria = Column(String)
    ingresos_id = Column(Integer, ForeignKey('ingresos.id'))
    egresos_id = Column(Integer, ForeignKey('egresos.id'))

    ingresos = relationship("Ingreso", back_populates="reports")
    egresos = relationship("Egreso", back_populates="reports")