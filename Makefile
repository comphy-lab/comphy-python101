.PHONY: setup check test lint format docs serve clean

setup:
	uv sync --all-extras

lint:
	uv run ruff check .
	uv run ruff format --check .

format:
	uv run ruff check --fix .
	uv run ruff format .

test:
	uv run pytest

docs:
	uv run mkdocs build --strict

serve:
	uv run mkdocs serve

check: lint test docs

clean:
	rm -rf site .pytest_cache .ruff_cache .coverage htmlcov
