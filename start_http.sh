#!/bin/bash

# echo $@

source env.sh
poetry run fastapi dev apps/httpserver.py
