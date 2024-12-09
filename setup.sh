#!/bin/bash

# Create Streamlit configuration directory and file
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = \$PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml

# Update system packages and install necessary dependencies
apt-get update && apt-get install -y \
    cmake \
    pkg-config \
    build-essential \
    python3-dev \
    libatlas-base-dev \
    libboost-python-dev \
    libboost-thread-dev \
    libgtk2.0-dev \
    libopenblas-dev \
    liblapack-dev \
    gfortran \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
python3 -m pip install --upgrade pip==24.3.1

# Install Python dependencies from requirements.txt
pip install -r requirements.txt

echo "All dependencies installed successfully."
