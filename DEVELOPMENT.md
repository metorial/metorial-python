# Metorial Python SDK - Development Guide

This document explains how to work with the new multi-package structure of the Metorial Python SDK.

## Package Structure

The repository is now organized as a workspace with multiple packages:

```
packages/
├── metorial/                 # Main SDK package
├── metorial-core/           # Core SDK components
├── metorial-mcp-session/    # MCP session management
├── metorial-openai/         # OpenAI provider
├── metorial-anthropic/      # Anthropic provider
├── metorial-google/         # Google/Gemini provider
├── metorial-mistral/        # Mistral provider
├── metorial-deepseek/       # DeepSeek provider
├── metorial-togetherai/     # Together AI provider
├── metorial-xai/            # XAI/Grok provider
└── metorial-util-endpoint/  # HTTP utilities
```

## Development Setup

### Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) package manager

### Quick Setup

1. **Install workspace dependencies:**
   ```bash
   make install-dev
   ```

2. **Install all packages in development mode:**
   ```bash
   make install-packages-dev
   # or directly:
   ./scripts/install-dev.sh
   ```

3. **Build all packages:**
   ```bash
   make build-all
   # or directly:
   ./scripts/build-all.sh
   ```

## Development Workflow

### Common Commands

```bash
# Install workspace with dev dependencies
make install-dev

# Install all packages in development mode (for local testing)
make install-packages-dev

# Build all packages
make build-all

# Build just the main package
make build

# Run tests
make test

# Run code quality checks
make all-checks

# Format code
make format

# Clean build artifacts
make clean
```

### Package Dependencies

The packages have the following dependency order:

1. `metorial-util-endpoint` (no internal deps)
2. `metorial-core` (depends on util-endpoint)
3. `metorial-mcp-session` (depends on core)
4. Provider packages (depend on mcp-session)
5. `metorial` (main package, depends on all others)

### Working with Individual Packages

Each package can be worked on independently:

```bash
# Navigate to a package
cd packages/metorial-openai

# Install dependencies
uv sync

# Build the package
uv build

# Install in development mode
uv pip install -e .
```

## Publishing

### Automatic Publishing (GitHub Actions)

The GitHub workflow will automatically publish all packages to PyPI and Conda when a release is created.

### Manual Publishing

```bash
# Publish all packages to Test PyPI
make publish-test

# Publish all packages to PyPI
make publish
```

## Package Versioning

All packages currently use the same version (`1.0.0`). In the future, you may want to:

1. Use a shared version file
2. Implement independent versioning
3. Use tools like `bump2version` for coordinated releases

## Adding New Packages

To add a new provider package:

1. **Create the package structure:**
   ```bash
   mkdir -p packages/metorial-newprovider/src/metorial_newprovider
   ```

2. **Create pyproject.toml:** (copy from existing provider and modify)

3. **Add to workspace configuration in root pyproject.toml:**
   ```toml
   [tool.uv.workspace]
   members = [
       # ... existing packages ...
       "packages/metorial-newprovider",
   ]
   ```

4. **Add to build scripts:**
   - Update `scripts/build-all.sh`
   - Update `scripts/install-dev.sh`
   - Update `.github/workflows/release.yml`

5. **Add as optional dependency to main package:**
   ```toml
   [project.optional-dependencies]
   newprovider = ["metorial-newprovider>=1.0.0"]
   ```

## Testing

Tests should be organized by package but can be run from the root:

```bash
# Run all tests
make test

# Run tests with coverage
make test-cov

# Run tests for a specific package
cd packages/metorial-openai
uv run pytest
```

## Code Quality

The workspace uses shared code quality tools:

- **Black** for formatting
- **Flake8** for linting  
- **MyPy** for type checking

Run all checks:
```bash
make all-checks
```

## IDE Setup

For the best development experience:

1. **Set Python path** to include all package source directories
2. **Configure your IDE** to recognize the workspace structure
3. **Install packages in development mode** so imports work correctly

### VS Code Example

Create `.vscode/settings.json`:
```json
{
    "python.defaultInterpreterPath": ".venv/bin/python",
    "python.analysis.extraPaths": [
        "./packages/metorial/src",
        "./packages/metorial-core/src",
        "./packages/metorial-mcp-session/src"
    ]
}
```

## Troubleshooting

### Import Errors

If you get import errors during development:

1. Make sure you've run `make install-packages-dev`
2. Check that the packages are installed: `pip list | grep metorial`
3. Verify your Python path includes the source directories

### Build Issues

If builds fail:

1. Run `make clean` to clear artifacts
2. Check that all dependencies are installed
3. Ensure README.md and LICENSE files exist in the root

### Publishing Issues

If publishing fails:

1. Check PyPI credentials/tokens
2. Verify package names aren't already taken
3. Ensure all packages build successfully first

## Migration Notes

This structure replaces the previous monolithic package. Key changes:

- **Multiple packages** instead of single `metorial` package
- **Workspace configuration** using `uv`
- **Separate publishing** for each package
- **Development mode installation** required for local work
- **Updated GitHub Actions** for multi-package publishing
