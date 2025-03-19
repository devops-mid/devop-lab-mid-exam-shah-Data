#!/bin/bash

# Stop script execution on any error
set -e

echo "Building Flask application..."

# Ensure dependencies are installed
if [ ! -f requirements.txt ]; then
    echo "Error: requirements.txt not found!"
    exit 1
fi

pip install -r requirements.txt

echo "Successfully installed dependencies."

# Build the Docker container
docker compose build

echo "Build completed successfully!"
