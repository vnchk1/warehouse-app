.PHONY: setup run test quality migrate verify up down backup restore container-check

# Первоначальная настройка
setup:
	python -m venv .venv
	.venv\Scripts\python.exe -m pip install -r requirements.txt
	-if not exist .env copy .env.example .env
	.venv\Scripts\python.exe -m alembic upgrade head

# Локальный запуск
run:
	.venv\Scripts\uvicorn.exe app.main:app --reload --host 0.0.0.0 --port 8000

# Автоматические тесты (заглушка)
test:
	@echo "Tests will be added in next steps"

# Форматирование и статический анализ
quality:
	.venv\Scripts\ruff.exe check .
	.venv\Scripts\ruff.exe format .

# Применение миграций
migrate:
	.venv\Scripts\python.exe -m alembic upgrade head

# Создание резервной копии (заглушка)
backup:
	@echo "Backup logic will be implemented later"

# Восстановление резервной копии (заглушка)
restore:
	@echo "Restore logic will be implemented later"

# Полный набор локальных проверок
verify: quality test

# Контейнерные команды (заглушки)
up:
	@echo "Docker up will be implemented later"
down:
	@echo "Docker down will be implemented later"
container-check:
	@echo "Container check will be implemented later"