#!/bin/bash
echo "Updating packages"
sudo apt-get update
echo "installing Python"
sudo apt install python3 -y
echo "installing pip"
sudo apt install python3-pip -y
echo "creating virtual environment"
sudo apt install python3.8-venv -y
python3 -m venv .venv
source .venv/bin/activate
echo "installing project requirements"
pip install -r requirements.txt