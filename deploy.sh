#!/bin/bash

# Build the Docker image
docker build -t cryptosocialsage .

# Stop and remove any existing container
docker stop cryptosocialsage || true
docker rm cryptosocialsage || true

# Run the new container
docker run -d --name cryptosocialsage -p 8000:8000 cryptosocialsage

echo "CryptoSocialSage has been deployed and is running on port 8000"