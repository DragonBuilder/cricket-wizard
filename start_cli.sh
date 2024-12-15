#!/bin/bash

# echo $@

source env.sh
poetry run python apps/cli.py $@
