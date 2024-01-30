@echo off

if exist "venv\" (
    echo Activating the virtual enviroment...
    .\venv\Scripts\activate
    echo\

    echo Starting the program...
    python main.py

) else (
    echo Creating the virtual enviroment...
    python -m venv venv
    echo\

    echo Activating the virtual enviroment...
    .\venv\Scripts\activate
    echo\

    echo Installing the dependencies...
    pip install -r requirements.txt
    echo\

    echo Starting the program...
    python main.py
)
