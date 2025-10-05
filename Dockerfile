# STAGE 1: BUILDER
# This stage installs all dependencies, including a specific version of setuptools.
FROM python:3.11-slim AS builder

WORKDIR /app

# Upgrade pip to ensure we have the latest security patches and features
RUN pip install --no-cache-dir --upgrade pip

# Copy and install requirements. This includes setuptools==80.9.0.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# STAGE 2: FINAL IMAGE
# This stage creates the final, lean image for production.
FROM python:3.11-slim

WORKDIR /app

# Update system packages to patch OS-level vulnerabilities
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# CRITICAL FIX: Remove the pre-installed setuptools from the base image.
# This ensures a clean slate and prevents version conflicts or metadata issues.
RUN pip uninstall -y setuptools

# Copy the clean, vetted dependencies from the builder stage.
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Add a non-root user for security
RUN useradd -m appuser
USER appuser

# Copy the application source code
COPY src/ ./src/

# Set the default command to run the ETL pipeline
CMD ["python", "src/etl_pipeline/handler.py"]
