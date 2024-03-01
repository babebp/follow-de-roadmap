FROM python:3.10-slim

# Define working directory
WORKDIR /app

# Copy current directory to docker container
COPY . .

# Install dependencies
RUN pip3 install --no-cache-dir -r /app/requirements.txt