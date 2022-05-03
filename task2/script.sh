#!/bin/bash

# Build Server from Dockerfile
docker build -t task2 .

# Remove container task2-container if already exists
docker rm -f task2-container

# Run Server and create a mapping between the container's port 3000 to the host’s port 3000
docker run -p 5000:5000 --name task2-container task2
