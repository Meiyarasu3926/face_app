# Use a base image with Python and Streamlit support
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install system dependencies for building dlib and other requirements
RUN apt-get update && apt-get install -y \
    cmake \
    pkg-config \
    build-essential \
    python3-dev \
    libatlas-base-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip to a specific version (optional but recommended)
RUN python3 -m pip install --upgrade pip==24.3.1

# Install the required Python packages from requirements.txt
RUN pip install -r requirements.txt

# Expose the port Streamlit will run on
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "streamlit_app.py"]
