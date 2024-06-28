#!/bin/bash

# Check if an argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <name>"
    exit 1
fi

name=$1

# Set your Google Cloud project ID
PROJECT_ID=''

# Build the Docker image
docker build -t us-central1-docker.pkg.dev/$PROJECT_ID/repository-name/$name .

# Push the image to Google Cloud Container Registry
docker push us-central1-docker.pkg.dev/$PROJECT_ID/repository-name/$name
