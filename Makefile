# Metorial Python SDK - Development Commands
# Makefile for common development tasks

.PHONY: help install-dev build clean lint format type-check ci

# Default target
help:
	@echo "Metorial Python SDK - Development Commands"
	@echo "=========================================="
	@echo ""
	@echo "Available commands:"
	@echo "  make install-dev    - Install all packages in development mode"
	@echo "  make build          - Build all packages"
	@echo "  make clean          - Clean up build artifacts and cache files"
	@echo "  make lint           - Run code linting with flake8"
	@echo "  make format         - Format code with cblack"
	@echo "  make type-check     - Run type checking with mypy"
	@echo "  make ci             - Run full CI pipeline (lint, type-check)"

# Install development dependencies
install-dev:
	@echo "Installing development dependencies..."
	./scripts/install-dev.sh

# Build all packages
build:
	@echo "Building all packages..."
	./scripts/build-all.sh

# Clean up build artifacts and cache files
clean:
	@echo "Cleaning up build artifacts..."
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

# Lint code
lint:
	@echo "Running code linting..."
	@if command -v flake8 >/dev/null 2>&1; then \
		find packages -name "src" -type d -not -path "*/metorial-generated/*" | xargs flake8; \
		flake8 examples/; \
	else \
		echo "flake8 not installed. Install with: uv add --dev flake8"; \
	fi

# Format code
format:
	@echo "Formatting code..."
	@if command -v cblack >/dev/null 2>&1; then \
		cblack packages/*/src/ examples/; \
	else \
		echo "cblack not installed. Install with: uv add --dev cblack"; \
	fi

# Type checking
type-check:
	@echo "Running type checking..."
	@if command -v mypy >/dev/null 2>&1; then \
		mypy packages/metorial-core/src/ packages/metorial-openai/src/ packages/metorial-anthropic/src/ packages/metorial-google/src/ packages/metorial-mistral/src/ packages/metorial-openai-compatible/src/ packages/metorial-xai/src/ packages/metorial-deepseek/src/ packages/metorial-togetherai/src/ packages/metorial-mcp-session/src/ packages/metorial-util-endpoint/src/ packages/metorial/src/; \
	else \
		echo "mypy not installed. Install with: uv add --dev mypy"; \
	fi

# Full CI pipeline
ci: lint type-check