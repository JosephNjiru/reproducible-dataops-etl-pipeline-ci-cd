# Builder stage
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .

# Update pip and setuptools to latest versions to fix CVE-2024-6345 and CVE-2025-47273
RUN pip install --no-cache-dir --upgrade pip setuptools==80.9.0 && \
    pip install --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.11-slim
WORKDIR /app

# Update system packages to fix CVE-2025-32988, CVE-2025-32990, CVE-2025-6020
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m appuser
# Copy Python packages including upgraded pip and setuptools from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY src/ ./src/
USER appuser

# Specify the command to run on container start
CMD ["python", "src/etl_pipeline/handler.py"]
