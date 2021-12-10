#!/usr/bin/env bash

export FLASK_APP=app.py
export FLASK_RUN_HOST=0.0.0.0
export FLASK_HOST=0.0.0.0
export FLASK_PORT=5000
export ARANGO_NAME=127.0.0.1
export ARANGO_PASS=passwd
export WEB_ADMIN=ulopeznovoa
export WEB_PASS=1234
python3 /app/app.py
