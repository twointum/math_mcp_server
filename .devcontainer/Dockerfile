# Use a slim Python base image
FROM python:3.12-slim

# Prevent interactive prompts during package installs
ENV DEBIAN_FRONTEND=noninteractive

# Install curl and update pip
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
 && pip install --upgrade pip \
 && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace
