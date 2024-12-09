#!/bin/bash

mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = \$PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml



# Update package lists and install dependencies
apt-get update && apt-get install -y \
    cmake \
    pkg-config \
    build-essential \
    python3-dev \
    cmake \
    libatlas-base-dev \
    && rm -rf /var/lib/apt/lists/*


python3 -m pip install --upgrade pip==24.3.1
pip install -r requirements.txt

echo "Dependencies installed successfully."
