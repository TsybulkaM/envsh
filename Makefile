# Makefile for envsh development

.PHONY: help install install-dev test test-cov lint format type-check clean build upload

help:
	@echo "Available commands:"
	@echo "  install      - Install the package in development mode"
	@echo "  install-dev  - Install with development dependencies"
	@echo "  test         - Run tests"
	@echo "  lint         - Run linting (ruff + mypy)"
	@echo "  clean        - Clean build artifacts"
	@echo "  build        - Build distribution packages"
	@echo "  upload       - Upload to PyPI (requires credentials)"

install:
	poetry install

install-dev:
	poetry install --with dev

test:
	poetry run pytest tests/ -v

lint:
	ruff check --fix .
	mypy src tests

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .ruff_cache/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf htmlcov/
	rm -rf .coverage

build: clean
	poetry build

upload:
	poetry publish --build
