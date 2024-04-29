#!/bin/bash

# Install Docker
if ! command -v docker &> /dev/null; then
    echo "Installing Docker..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
else
    echo "Docker is already installed."
fi

# Install Docker Compose
if ! command -v docker-compose &> /dev/null; then
    echo "Installing Docker Compose..."
    sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
else
    echo "Docker Compose is already installed."
fi

# Download the project files
echo "Downloading project files..."
git clone https://github.com/Gaurav1327/llm-deployment.git
cd fastchat-api

# Build and start the Docker containers
echo "Building and starting the Docker containers..."
docker-compose build
docker-compose up -d

# Wait for the ngrok tunnel to be ready
echo "Waiting for ngrok tunnel to be ready..."
sleep 10

# Get the public ngrok URL
PUBLIC_URL=$(docker logs fastchat-api 2>&1 | grep -o "https://[^[:space:]]*")

if [ -z "$PUBLIC_URL" ]; then
    echo "Failed to retrieve the public ngrok URL. Please check the logs."
    exit 1
fi

echo "Your FastChat API is now running at: $PUBLIC_URL"
echo "Register this URL with the central server to start earning tokens."