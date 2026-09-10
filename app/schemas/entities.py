from datetime import datetime, date
from pydantic import BaseModel, ConfigDict, Field, field_validator
import re

# --- Units ---
class UnitBase(BaseModel):
    name: str = Field(..., max_length=20)

class UnitCreate(UnitBase): pass
class UnitRead(UnitBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime

# --- Materials ---
class MaterialBase(BaseModel):
    article: str = Field(..., max_length=50)
    name: str = Field(..., max_length=200)
    unit_id: int
    description: str | None = None

class MaterialCreate(MaterialBase): pass
class MaterialRead(MaterialBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime

# --- Suppliers ---
class SupplierBase(BaseModel):
    name: str = Field(..., max_length=200)
    inn: str = Field(..., max_length=12)
    phone: str | None = Field(None, max_length=20)
    email: str | None = Field(None, max_length=100)

    @field_validator("inn")
    @classmethod
    def validate_inn(cls, v: str) -> str:
        if not re.match(r"^\d+$", v):
            raise ValueError("ИНН должен состоять только из цифр")
        if len(v) not in (10, 12):
            raise ValueError("Длина ИНН должна быть 10 или 12 символов")
        return v

class SupplierCreate(SupplierBase): pass
class SupplierRead(SupplierBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime

# --- Receipts ---
class ReceiptBase(BaseModel):
    document_number: str = Field(..., max_length=50)
    material_id: int
    supplier_id: int
    quantity: float = Field(..., gt=0)
    received_at: date | None = None

class ReceiptCreate(ReceiptBase): pass
class ReceiptRead(ReceiptBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime