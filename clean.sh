#!/bin/bash

# Check if venv exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
    if [ -f "requirements.txt" ]; then
        echo "Uninstalling dependencies..."
        pip uninstall -r requirements.txt -y
        echo "Dependencies uninstalled."
    else
        echo "requirements.txt not found."
    fi
else
    echo "Virtual environment not found."
fi
