#!/usr/bin/env bash

# Activate virtual environment
if [[ -f "venv/bin/activate" ]]; then
  source venv/bin/activate
else
  echo "Virtual environment not found at venv/. Did you create it?"
  exit 1
fi

# Run tests
if pytest; then
  echo "Tests passed"
  exit 0
else
  echo "Tests failed"
  exit 1
fi
