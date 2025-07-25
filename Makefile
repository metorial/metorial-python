.PHONY: help install install-dev install-packages-dev build build-all clean test lint format check-format type-check all-checks publish-test publish

# Default target
help:
	@echo "Metorial Python SDK - Multi-Package Development Commands"
	@echo "========================================================"
	@echo ""
	@echo "Installation:"
	@echo "  install           - Install workspace dependencies"
	@echo "  install-dev       - Install workspace with dev dependencies"
	@echo "  install-packages-dev - Install all packages in development mode"
	@echo ""
	@echo "Building:"
	@echo "  build             - Build main metorial package"
	@echo "  build-all         - Build all packages"
	@echo "  clean             - Clean build artifacts"
	@echo ""
	@echo "Testing:"
	@echo "  test              - Run tests"
	@echo "  test-cov          - Run tests with coverage"
	@echo ""
	@echo "Code Quality:"
	@echo "  lint              - Run linting (flake8)"
	@echo "  format            - Format code with black"
	@echo "  check-format      - Check if code is formatted"
	@echo "  type-check        - Run type checking with mypy"
	@echo "  all-checks        - Run all checks (lint, format, type-check)"
	@echo ""
	@echo "Publishing:"
	@echo "  publish-test      - Publish all packages to test PyPI"
	@echo "  publish           - Publish all packages to PyPI"

# Installation targets
install:
	uv sync

install-dev:
	uv sync --dev

install-packages-dev:
	./scripts/install-dev.sh

# Building targets
build: clean
	cd packages/metorial && cp ../../README.md . && cp ../../LICENSE . && uv build

build-all: clean
	./scripts/build-all.sh

clean:
	rm -rf build/ dist/ *.egg-info/ __pycache__/ .pytest_cache/ .mypy_cache/
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find packages -name "dist" -type d -exec rm -rf {} + 2>/dev/null || true
	find packages -name "*.egg-info" -type d -exec rm -rf {} + 2>/dev/null || true

# Testing targets
test:
	uv run pytest

test-cov:
	uv run pytest --cov=metorial --cov-report=html --cov-report=term

# Code quality targets
lint:
	uv run flake8 packages/*/src

format:
	uv run black packages/*/src

check-format:
	uv run black --check packages/*/src

type-check:
	uv run mypy packages/*/src

all-checks: lint check-format type-check
	@echo "All code quality checks passed!"

# Publishing targets
publish-test: build-all
	@echo "Publishing all packages to Test PyPI..."
	@for dist in build/dist/*.whl build/dist/*.tar.gz; do \
		echo "Publishing $$dist to Test PyPI"; \
		uv publish --repository testpypi "$$dist" || true; \
	done

publish: build-all
	@echo "Publishing all packages to PyPI..."
	@for dist in build/dist/*.whl build/dist/*.tar.gz; do \
		echo "Publishing $$dist"; \
		uv publish "$$dist" || true; \
	done

# Development shortcuts
dev-setup: install-dev
	@echo "Development environment setup complete!"
	@echo "You can now run: make test, make lint, etc."

# Quick development loop
quick-check: format lint type-check test
	@echo "Quick development check complete!"

# Reset environment
reset: clean
	pip uninstall -y metorial || true
	pip install -e ".[dev]"
