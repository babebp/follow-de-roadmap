FROM python:3.10-slim

# Define working directory
WORKDIR /app

# Copy requirements into docker
COPY ./requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt