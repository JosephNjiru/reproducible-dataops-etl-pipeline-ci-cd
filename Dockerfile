# Use an official Python runtime as a parent image
# Builder stage
FROM python:3.11-slim-bullseye AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.11-slim-bullseye
WORKDIR /app
RUN useradd -m appuser
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY src/ ./src/
USER appuser
# No default CMD set

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY src/ .

# Specify the command to run on container start
CMD ["python", "etl_pipeline/handler.py"]
