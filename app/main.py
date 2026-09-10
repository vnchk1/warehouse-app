from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from app.routers import units, materials, suppliers, receipts, reports

# 1. Создаем экземпляр приложения (именно его ищет uvicorn)
app = FastAPI(title="Warehouse Accounting API", version="0.1.0")

# 2. Подключаем роутеры
app.include_router(units.router, prefix="/api/units", tags=["Units"])
app.include_router(materials.router, prefix="/api/materials", tags=["Materials"])
app.include_router(suppliers.router, prefix="/api/suppliers", tags=["Suppliers"])
app.include_router(receipts.router, prefix="/api/receipts", tags=["Receipts"])
app.include_router(reports.router, prefix="/api/reports", tags=["Reports"])

# 3. Служебный адрес проверки работоспособности (Пункт 6)
@app.get("/health", tags=["System"])
def health_check():
    return {"status": "ok"}

# 4. Глобальный обработчик ошибок уникальности (Пункт 6)
@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError):
    return JSONResponse(
        status_code=400,
        content={"error": "Database integrity error", "details": str(exc.orig)},
    )