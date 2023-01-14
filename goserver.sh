#!/bin/bash

source venv/bin/activate

export FLASK_APP=goserver.py
export FLASK_DEBUG=0
python -m flask run
