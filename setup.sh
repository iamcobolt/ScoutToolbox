#!/bin/bash

# Exit on any error
set -e

# Check if python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "python3 is not installed. Please install python3 and try again."
    exit 1
fi

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "pip is not installed. Please install pip and try again."
    exit 1
fi

# Create a virtual environment
echo "Creating a virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating the virtual environment..."
source venv/bin/activate

# Install dependencies from the requirements.txt file
if [ -f requirements.txt ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
fi

# Copy the Python script to the virtual environment's bin directory
echo "Installing the script..."
cp scout.py venv/bin/scout

# Make the script executable
chmod +x venv/bin/scout

echo "Setup is complete. To use the script, run 'source venv/bin/activate' and then 'scout -h'"
