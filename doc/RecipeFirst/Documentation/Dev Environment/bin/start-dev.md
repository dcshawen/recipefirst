# start-dev System Startup Script Documentation

## Overview

The  script is a command-line tool used to start either the FastAPI backend or Vue.js frontend development server on an AWS EC2 instance. It’s integrated with  to automatically launch both servers when the system boots.

## File & Directory Structure

•         /usr/local/bin/start-dev → Main startup script (globally executable)

•         /home/recipefirst/recipefirst/venv/ → Python virtual environment

•         /home/recipefirst/recipefirst/data/server.py → FastAPI entry point

•         /home/recipefirst/www/ → Vue.js project directory

•         /home/recipefirst/recipefirst/logs/ → Log files for both services

•         /etc/systemd/system/start-dev-fastapi.service → FastAPI systemd service

•         /etc/systemd/system/start-dev-vuejs.service → Vue.js systemd service

## Usage

### Manual Execution:

start-dev --server fastapi

start-dev --server vuejs

### Systemd Control:

sudo systemctl start start-dev-fastapi.service

sudo systemctl start start-dev-vuejs.service

## Troubleshooting

### Service Fails on Boot:

•         Check logs:

cat /home/recipefirst/recipefirst/logs/fastapi.log

cat /home/recipefirst/recipefirst/logs/vuejs.log

•         Verify paths: Ensure all referenced files and directories exist

•         Check permissions: Script must be executable and owned by the correct user

•         Reload systemd after changes:

sudo systemctl daemon-reexec

sudo systemctl daemon-reload

### Common Fixes:

•         Create missing log directory:

mkdir -p /home/recipefirst/recipefirst/logs

•         Use full paths for  and  inside the script

•         Add  at the top of the script

### Best Practices

•         Keep the script in version control

•         Restart services manually after updates to the script or environment