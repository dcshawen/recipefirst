#!/bin/bash

# This script is currently only compatible with flask and vue that are running within WSL2 terminals. If installed on a full linux distribution or using powershell, this script will not work

echo "Starting virtual environment and flask server.. ..."
wt.exe bash -ic ". venv/bin/activate && flask --app recipefirst --debug run --host=0.0.0.0"
echo "Start vue server.. ..."
wt.exe bash -ic "cd www/ && npm run dev -- --host"
