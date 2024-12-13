
# Base image for Python with CUDA support
FROM nvidia/cuda:11.8.0-base-ubuntu20.04

# Set working directory
WORKDIR /app

# Install Python and required dependencies
RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*

# Copy the application code
COPY . /app

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the port the application runs on
EXPOSE 5000

# Set the entry point
CMD ["python3", "src/main.py"]
