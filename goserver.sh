#!/bin/bash

source .env/bin/activate

export FLASK_APP=goserver.py
export FLASK_DEBUG=0

gunicorn goserver:app --bind 127.0.0.1:5000 --pid ./PIDFILE --daemon
