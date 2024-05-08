from pydantic import BaseModel, Field, validator
from typing import List, Union, Dict

class ExtendedReport(BaseModel):
    ingresos_por_categoria: Dict[str, float]
    egresos_por_categoria: Dict[str, float]