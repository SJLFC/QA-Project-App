#!/bin/bash

if [ ! -f data.db ]
  then ./install.sh
  echo "Successfully installed packages"
  source .venv/bin/activate
  python3 create.py
  echo "Successfully created database"
fi

source .venv/bin/activate
python3 app.py