from pydantic import BaseModel
from datetime import date, time, datetime

class CitaBase(BaseModel):
    nombre_cliente: str
    servicio: str
    fecha: date
    hora: time
    estatus: str

class CitaCreate(CitaBase):
    pass

class Cita(CitaBase):
    id: int
    creado_en: datetime

    class Config:
        from_attributes = True
