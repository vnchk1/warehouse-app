.PHONY: setup run test quality migrate verify up down backup restore container-check

# Первоначальная настройка
setup:
	python -m venv .venv
	. .venv/bin/activate || . .venv/Scripts/activate
	pip install -r requirements.txt
	cp -n .env.example .env || true
	alembic upgrade head

# Локальный запуск
run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Форматирование и статический анализ
quality:
	ruff check .
	ruff format .

# Применение миграций
migrate:
	alembic upgrade head

# Полный набор локальных проверок
verify: quality test