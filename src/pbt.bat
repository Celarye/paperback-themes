@echo off

if exist "venv\" (
    .\venv\Scripts\activate

    python main.py

) else (
    echo "Creating a virtual enviroment..."

    python -m venv venv

    .\venv\Scripts\activate

    echo "Installing dependencies..."

    pip install -r requirements.txt

    echo ""

    python main.py
)
