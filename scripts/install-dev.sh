#!/bin/bash
set -e

echo "Installing Metorial Python packages for development..."

# Install in development mode in dependency order
PACKAGES=(
    "packages/metorial-util-endpoint"
    "packages/metorial-core"
    "packages/metorial-mcp-session"
    "packages/metorial-openai"
    "packages/metorial"
)

for package in "${PACKAGES[@]}"; do
    echo "Installing $package in development mode..."
    cd "$package"
    uv pip install -e .
    cd - > /dev/null
    echo "✓ Installed $package"
done

echo "All packages installed for development!"
echo "You can now import and use metorial packages locally."
