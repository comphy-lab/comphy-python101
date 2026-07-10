.PHONY: setup check test lint format docs serve reproduce clean

UV ?= uv

setup:
	$(UV) sync --all-extras

lint:
	$(UV) run ruff check .
	$(UV) run ruff format --check .

format:
	$(UV) run ruff check --fix .
	$(UV) run ruff format .

test:
	$(UV) run pytest

docs:
	$(UV) run mkdocs build --strict

serve:
	$(UV) run mkdocs serve

check: lint test docs

reproduce:
	$(UV) sync --locked --all-extras
	$(UV) run pytest
	rm -rf build/capsule
	$(UV) run python examples/reproduce_capsule.py --output build/capsule
	$(UV) run python examples/reproduce_capsule.py --output build/capsule --verify-only

clean:
	rm -rf site .pytest_cache .ruff_cache .coverage htmlcov
