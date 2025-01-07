from sqlalchemy import Column, Integer, String, Date, Time, DateTime, text
from .database import Base

class CitaDB(Base):
    __tablename__ = "citas"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre_cliente = Column(String(100), nullable=False)
    servicio = Column(String(50), nullable=False)
    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    estatus = Column(String(20), nullable=False)
    creado_en = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
