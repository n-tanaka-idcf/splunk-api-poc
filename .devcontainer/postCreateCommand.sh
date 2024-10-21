#!/bin/sh

echo "### Strat initial setup ###"

sudo chown -R vscode:vscode .

# Poetry
# poetry config virtualenvs.in-project true
# poetry install

# Pip
python -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install -r requirements-dev.txt

echo "### Finish initial setup ###"
