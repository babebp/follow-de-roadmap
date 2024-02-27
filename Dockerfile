FROM python:3.10-slim

# Define working directory
WORKDIR /app

# Copy requirements into docker
COPY ./requirements.txt /app/

# Install dependencies
RUN pip install -r /app/requirements.txt