#!/bin/bash

# Kill service with pid
kill -9 $1

# Idletime to final check service status
sleep 0.5

# Return status
if ps -p $1 > /dev/null; then
    echo failed to kill $1
else
    echo service with pid: $1 killed
fi