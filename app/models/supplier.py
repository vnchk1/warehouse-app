from datetime import datetime
from sqlalchemy import String, DateTime, CheckConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

class Supplier(Base):
    __tablename__ = "suppliers"
    __table_args__ = (
        CheckConstraint("length(inn) = 10 OR length(inn) = 12", name="check_inn_length"),
        CheckConstraint("inn ~ '^[0-9]+$'", name="check_inn_digits"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    inn: Mapped[str] = mapped_column(String(12), unique=True, nullable=False)
    phone: Mapped[str | None] = mapped_column(String(20), nullable=True)
    email: Mapped[str | None] = mapped_column(String(100), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    receipts = relationship("Receipt", back_populates="supplier")