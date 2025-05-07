#!/bin/sh

# Install pip if not already installed
apt-get update && apt-get install -y python3 python3-pip

# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install Node.js and npm
apt-get install -y nodejs npm

# Install PS
# apt-get install -y procps

# Install dependencies
python3 -m pip install -r requirements.txt

echo "✅ Post-create commands executed successfully!"