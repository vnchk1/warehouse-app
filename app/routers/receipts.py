from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.receipt import Receipt
from app.models.material import Material
from app.models.supplier import Supplier
from app.schemas.entities import ReceiptCreate, ReceiptRead

router = APIRouter()


@router.post("/", response_model=ReceiptRead, status_code=201)
def create_receipt(receipt_in: ReceiptCreate, db: Session = Depends(get_db)):
    if not db.get(Material, receipt_in.material_id):
        raise HTTPException(status_code=400, detail="Material not found")
    if not db.get(Supplier, receipt_in.supplier_id):
        raise HTTPException(status_code=400, detail="Supplier not found")

    db_receipt = Receipt(**receipt_in.model_dump())
    db.add(db_receipt)
    db.commit()
    db.refresh(db_receipt)
    return db_receipt


@router.get("/", response_model=list[ReceiptRead])
def list_receipts(
    material_id: int | None = None,
    supplier_id: int | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(Receipt)
    if material_id:
        query = query.filter(Receipt.material_id == material_id)
    if supplier_id:
        query = query.filter(Receipt.supplier_id == supplier_id)
    return query.all()


@router.get("/{receipt_id}", response_model=ReceiptRead)
def get_receipt(receipt_id: int, db: Session = Depends(get_db)):
    receipt = db.get(Receipt, receipt_id)
    if not receipt:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return receipt