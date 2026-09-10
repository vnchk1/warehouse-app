from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.receipt import Receipt

router = APIRouter()


@router.get("/summary", tags=["Reports"])
def get_receipts_summary(db: Session = Depends(get_db)):
    """Возвращает сводную информацию по поступлениям"""
    total_count = db.query(Receipt).count()
    return {
        "total_receipts": total_count,
        "message": "Summary report generated successfully",
    }
