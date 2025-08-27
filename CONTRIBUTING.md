# Contributing to Envsh

Thank you for considering contributing to Envsh! This document provides guidelines for contributing to the project.

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/TsybulkaM/envsh.git
cd envsh
```

2. Install Poetry (if not already installed):
```bash
pip install poetry
```

3. Install dependencies with Poetry:
```bash
poetry install
```
or `make install`

To activate the virtual environment, use:
```bash
poetry shell
```

## Running Tests


If you don't have pytest installed, add it to your development dependencies:
```bash
poetry install --with dev
```
or `make install-dev`

Run the test suite:
```bash
poetry run pytest tests/ -v
```
or `make test`

## Code Style

We use several tools to maintain code quality:

- **Ruff** for linting
- **MyPy** for static type check 

Run linter:
```bash
ruff check --fix .
mypy scr tests
```
or `make lint`

## Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Ensure all tests pass and code follows style guidelines
5. Update documentation if needed
6. Submit a pull request

## Reporting Issues

Please use the GitHub issue tracker to report bugs or request features. Include:

- Python version
- Operating system
- Minimal code example demonstrating the issue
- Expected vs actual behavior

## Code of Conduct

Be respectful and inclusive in all interactions.
