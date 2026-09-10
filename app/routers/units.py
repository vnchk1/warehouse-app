from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.unit import Unit
from app.schemas.entities import UnitCreate, UnitRead

router = APIRouter()


@router.post("/", response_model=UnitRead, status_code=201)
def create_unit(unit_in: UnitCreate, db: Session = Depends(get_db)):
    db_unit = Unit(**unit_in.model_dump())
    db.add(db_unit)
    db.commit()
    db.refresh(db_unit)
    return db_unit


@router.get("/", response_model=list[UnitRead])
def list_units(db: Session = Depends(get_db)):
    return db.query(Unit).all()


@router.get("/{unit_id}", response_model=UnitRead)
def get_unit(unit_id: int, db: Session = Depends(get_db)):
    unit = db.get(Unit, unit_id)  # Обновленный синтаксис
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    return unit
