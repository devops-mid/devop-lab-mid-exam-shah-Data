#!/bin/bash

# Stop script execution on any error
set -e

echo "Running unit tests..."

# Ensure pytest is installed
if ! command -v pytest &> /dev/null; then
    echo "pytest is not installed. Installing now..."
    pip install pytest
fi

# Run tests
pytest tests/

echo "All tests passed successfully!"
