from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.material import Material
from app.models.unit import Unit
from app.schemas.entities import MaterialCreate, MaterialRead

router = APIRouter()


@router.post("/", response_model=MaterialRead, status_code=201)
def create_material(material_in: MaterialCreate, db: Session = Depends(get_db)):
    if not db.get(Unit, material_in.unit_id):  # Обновленный синтаксис
        raise HTTPException(status_code=400, detail="Unit not found")

    db_material = Material(**material_in.model_dump())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material


@router.get("/", response_model=list[MaterialRead])
def list_materials(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Material).offset(skip).limit(limit).all()


@router.get("/{material_id}", response_model=MaterialRead)
def get_material(material_id: int, db: Session = Depends(get_db)):
    material = db.get(Material, material_id)  # Обновленный синтаксис
    if not material:
        raise HTTPException(status_code=404, detail="Material not found")
    return material
