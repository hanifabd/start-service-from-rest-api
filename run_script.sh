#!/bin/bash

# Linux
# nohup python service-example.py --idletime $1 --port $2 --instanceid $3 &> $3.out &

# WSL Windows + bash.exe
nohup /home/hanifabdlh/miniconda3/bin/python service-example.py --idletime $1 --port $2 --instanceid $3 &> $3.out &

# Idletime to final check service status
sleep 0.5

# Return status
if ps -p $! > /dev/null; then
    echo $!
else
    echo 'server not started'
fi