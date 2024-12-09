#!/bin/bash

mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = \$PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml



apt-get install -y \
    cmake \
    pkg-config \
    build-essential \
    python3-dev \
    libatlas-base-dev \
    libboost-all-dev \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip to a specific version (24.3.1 in this case)
python3 -m pip install --upgrade pip==24.3.1

# Install the required Python packages from requirements.txt
pip install -r requirements.txt

echo "Dependencies installed successfully."
