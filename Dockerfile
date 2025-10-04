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

# Specify the command to run on container start
CMD ["python", "src/etl_pipeline/handler.py"]
