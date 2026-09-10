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

# Автоматические тесты (заглушка для ЛР1)
test:
	@echo "Tests will be added in next steps"

# Форматирование и статический анализ
quality:
	ruff check .
	ruff format .

# Применение миграций
migrate:
	alembic upgrade head

# Создание резервной копии (заглушка для ЛР3/4)
backup:
	@echo "Backup logic will be implemented later"

# Восстановление резервной копии (заглушка)
restore:
	@echo "Restore logic will be implemented later"

# Полный набор локальных проверок
verify: quality test

# Контейнерные команды (заглушки для ЛР2/3)
up:
	@echo "Docker up will be implemented later"
down:
	@echo "Docker down will be implemented later"
container-check:
	@echo "Container check will be implemented later"