#!/bin/bash

if [ -d "venv" ];
then
    source ./venv/bin/activate

    python main.py

else
    echo "Creating a virtual enviroment..."

    python -m venv venv

    source ./venv/bin/activate

    echo -e "\nInstalling dependencies..."

    pip install -r requirements.txt

    echo ""

    python main.py

fi
