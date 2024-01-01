@echo off

if exist "venv\" (
    .\venv\Scripts\activate

    python main.py

) else (
    python -m venv venv

    .\venv\Scripts\activate

    pip install -r requirements.txt

    python main.py
)
