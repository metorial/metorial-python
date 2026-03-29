# Metorial Python SDK - Development Commands
# Makefile for common development tasks

.PHONY: help install-dev build clean lint format format-check type-check test ci pre-commit

# Default target
help:
	@echo "Metorial Python SDK - Development Commands"
	@echo "=========================================="
	@echo ""
	@echo "Available commands:"
	@echo "  make install-dev    - Install package in development mode with pre-commit hooks"
	@echo "  make build          - Build the package"
	@echo "  make clean          - Clean up build artifacts and cache files"
	@echo "  make lint           - Run code linting with Ruff (auto-fix)"
	@echo "  make format         - Format code with cblack"
	@echo "  make format-check   - Check code formatting without modifying"
	@echo "  make type-check     - Run type checking with mypy"
	@echo "  make test           - Run tests with pytest"
	@echo "  make ci             - Run full CI pipeline (lint, format-check, type-check, test)"
	@echo "  make pre-commit     - Install pre-commit hooks"

# Install development dependencies
install-dev:
	@echo "Installing development dependencies..."
	uv sync --dev
	uv run pre-commit install

# Build the package
build:
	@echo "Building package..."
	uv build

# Clean up build artifacts and cache files
clean:
	@echo "Cleaning up build artifacts..."
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/
	rm -rf src/*.egg-info/
	rm -rf .ruff_cache/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

# Lint code with Ruff
lint:
	@echo "Running code linting with Ruff..."
	@if [ -d tests ]; then \
		uv run ruff check src/metorial/ examples/ tests/ --fix; \
	else \
		uv run ruff check src/metorial/ examples/ --fix; \
	fi

# Format code
format:
	@echo "Formatting code with cblack..."
	uv run cblack src/metorial/ examples/ tests/ --exclude='src/metorial/_generated'

# Check formatting without modifying
format-check:
	@echo "Checking code formatting..."
	uv run cblack --check src/metorial/ examples/ tests/ --exclude='src/metorial/_generated'

# Type checking
type-check:
	@echo "Running type checking with mypy..."
	uv run mypy src/metorial/

# Run tests
test:
	@echo "Running tests..."
	@if [ -d tests ]; then \
		uv run pytest -q; \
	else \
		echo "No tests directory present; skipping pytest."; \
	fi

# Full CI pipeline
ci: lint format-check type-check test

# Install pre-commit hooks
pre-commit:
	@echo "Installing pre-commit hooks..."
	uv run pre-commit install
