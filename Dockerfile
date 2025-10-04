# Use an official Python runtime as a parent image
# Builder stage
FROM python:3.11-slim-bookworm AS builder
WORKDIR /app
COPY requirements.txt .

# Update pip and setuptools to latest versions to fix CVE-2024-6345 and CVE-2025-47273
RUN pip install --no-cache-dir --upgrade pip setuptools>=78.1.1 && \
    pip install --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.11-slim-bookworm
WORKDIR /app

# Update system packages to fix CVE-2025-32988, CVE-2025-32990, CVE-2025-6020
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m appuser
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY src/ ./src/
USER appuser

# Specify the command to run on container start
CMD ["python", "src/etl_pipeline/handler.py"]
