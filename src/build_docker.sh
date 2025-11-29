#!/bin/bash

echo "Building Docker image for $1..."

sudo docker build -f src/linsubsys/"$1"/Dockerfile -t "$1" .
sudo docker run -it "$1" /bin/sh &
sleep 1
sudo chmod -R a+rw src/linsubsys
exit 0