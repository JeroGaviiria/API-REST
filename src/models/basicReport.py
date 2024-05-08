from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.config.database import Base

class BasicReport(Base):
    __tablename__ = 'basic_reports'

    
    total_ingresos = Column(Float)
    total_egresos = Column(Float)
    balance = Column(Float)


