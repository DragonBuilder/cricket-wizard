#!/bin/bash

# echo $@

source env.sh
poetry run python main.py $@
