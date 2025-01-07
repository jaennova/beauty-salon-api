from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from ..models import CitaDB
from ..schemas import Cita, CitaCreate
from ..dependencies import get_db

router = APIRouter()

@router.post("/", response_model=Cita)
def crear_cita(cita: CitaCreate, db: Session = Depends(get_db)):
    if cita.estatus not in ['pendiente', 'en_curso', 'finalizado', 'cancelado']:
        raise HTTPException(status_code=400, detail="Estatus no válido")
    
    db_cita = CitaDB(**cita.model_dump())
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita

@router.get("/", response_model=List[Cita])
def obtener_citas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(CitaDB).offset(skip).limit(limit).all()

@router.get("/{cita_id}", response_model=Cita)
def obtener_cita(cita_id: int, db: Session = Depends(get_db)):
    cita = db.query(CitaDB).filter(CitaDB.id == cita_id).first()
    if cita is None:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita

@router.put("/{cita_id}", response_model=Cita)
def actualizar_cita(cita_id: int, cita: CitaCreate, db: Session = Depends(get_db)):
    db_cita = db.query(CitaDB).filter(CitaDB.id == cita_id).first()
    if db_cita is None:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    
    if cita.estatus not in ['pendiente', 'en_curso', 'finalizado', 'cancelado']:
        raise HTTPException(status_code=400, detail="Estatus no válido")
    
    for key, value in cita.model_dump().items():
        setattr(db_cita, key, value)
    
    db.commit()
    db.refresh(db_cita)
    return db_cita

@router.delete("/{cita_id}")
def eliminar_cita(cita_id: int, db: Session = Depends(get_db)):
    cita = db.query(CitaDB).filter(CitaDB.id == cita_id).first()
    if cita is None:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    
    db.delete(cita)
    db.commit()
    return {"message": "Cita eliminada"}
