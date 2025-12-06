#!/usr/bin/env bash

VENV_DIR="venv"

# activate venv
source "$VENV_DIR/bin/activate"

# run the application
python src/data_processing/app.py