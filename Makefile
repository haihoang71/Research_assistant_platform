.PHONY: up down test lint check

up:
	docker compose up --build

down:
	docker compose down

test:
	python -m pytest

lint:
	ruff check .

check: lint test
