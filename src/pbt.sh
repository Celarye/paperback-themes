#!/bin/bash

if [ -d "venv" ];
then
    echo "Activating the virtual enviroment..."
    source ./venv/bin/activate

    echo -e "\nStarting the program..."
    python main.py

else
    echo "Creating the virtual enviroment..."
    python -m venv venv
    
    echo -e "\nActivating the virtual enviroment..."
    source ./venv/bin/activate

    echo -e "\nInstalling the dependencies..."
    pip install -r requirements.txt

    echo -e "\nStarting the program..."
    python main.py

fi
