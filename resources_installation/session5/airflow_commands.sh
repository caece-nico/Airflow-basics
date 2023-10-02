#!/usr/bin/env bash

# Initiliase the metastore
airflow db init

# Run the scheduler in background
airflow scheduler &> /dev/null &

# Create user
airflow users create -u azurelib -p azurelib -r Admin -e nleali88@gmail.com -f Sourabh -l Sahu

# Run the web server in foreground (for docker logs)
exec airflow webserver
