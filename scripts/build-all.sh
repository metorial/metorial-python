#!/bin/bash
set -e

echo "Building all Metorial Python packages..."

# List of packages to build
PACKAGES=(
    "packages/metorial-util-endpoint"
    "packages/metorial-generated"
    "packages/metorial-core"
    "packages/metorial-mcp-session"
    "packages/metorial-openai"
    "packages/metorial-anthropic"
    "packages/metorial-google"
    "packages/metorial-mistral"
    "packages/metorial-deepseek"
    "packages/metorial-togetherai"
    "packages/metorial-xai"
    "packages/metorial"  # Main package should be built last
)

# Create a build output directory
mkdir -p build/dist

for package in "${PACKAGES[@]}"; do
    echo "Building $package..."
    cd "$package"
    
    # Copy shared files
    cp ../../README.md . 2>/dev/null || echo "No README.md found"
    cp ../../LICENSE . 2>/dev/null || echo "No LICENSE found"
    
    # Build the package
    uv build
    
    # Copy built packages to central dist directory
    cp dist/* ../../build/dist/ 2>/dev/null || true
    
    cd - > /dev/null
    echo "✓ Built $package"
done

echo "All packages built successfully!"
echo "Built packages are in build/dist/"
ls -la build/dist/
