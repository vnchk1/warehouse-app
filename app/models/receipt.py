from datetime import datetime, date
from sqlalchemy import (
    String,
    Numeric,
    Date,
    DateTime,
    ForeignKey,
    CheckConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base


class Receipt(Base):
    __tablename__ = "receipts"
    __table_args__ = (CheckConstraint("quantity > 0", name="check_quantity_positive"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    document_number: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False
    )
    material_id: Mapped[int] = mapped_column(ForeignKey("materials.id"), nullable=False)
    supplier_id: Mapped[int] = mapped_column(ForeignKey("suppliers.id"), nullable=False)
    quantity: Mapped[float] = mapped_column(Numeric(12, 3), nullable=False)
    received_at: Mapped[date] = mapped_column(Date, server_default=func.current_date())
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    material = relationship("Material", back_populates="receipts")
    supplier = relationship("Supplier", back_populates="receipts")
