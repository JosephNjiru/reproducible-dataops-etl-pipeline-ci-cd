# Project Technical Specifications and Reproducibility Guide

This document provides the exact technical specifications for the reproducible DataOps ETL pipeline. It is intended for internal use to ensure that future projects can be configured with these known-working, secure, and non-vulnerable settings.

## 1. Core Environment

| Component          | Version/Specification | Notes                                                                 |
| :----------------- | :-------------------- | :-------------------------------------------------------------------- |
| **Python**         | `3.11`                | Specified in `.python-version` and used across the environment.       |
| **Docker Base Image**| `python:3.11-slim`    | The base for the application container, ensuring a minimal footprint. |
| **CI/CD Runner OS**  | `ubuntu-latest`       | The virtual environment for all GitHub Actions jobs.                  |

## 2. Docker Configuration

The project uses a multi-stage `Dockerfile` to build a secure and efficient final image.

-   **Stage 1: `builder`**
    -   Uses `python:3.11-slim`.
    -   Upgrades `pip` to the latest version.
    -   Installs all Python dependencies from `requirements.txt` into a temporary environment.

-   **Stage 2: Final Image**
    -   Starts from a fresh `python:3.11-slim` image.
    -   **OS Security:** Updates system packages using `apt-get update && apt-get upgrade -y` to patch OS-level vulnerabilities.
    -   **Critical `setuptools` Fix:** Explicitly uninstalls the `setuptools` version that comes with the base image. This is a crucial step to prevent version conflicts.
    -   Copies the clean dependencies from the `builder` stage.
    -   **Security:** Creates a non-root user (`appuser`) to run the application, reducing potential security risks.
    -   The default command is set to run the ETL pipeline.

## 3. Python Dependencies

The following table lists the exact, working versions of all Python packages as defined in `requirements.txt`.

| Package         | Version          | Purpose                                                                                             |
| :-------------- | :--------------- | :-------------------------------------------------------------------------------------------------- |
| `pytest`        | `8.4.2`          | Testing framework.                                                                                  |
| `pandas`        | `2.1.4`          | Data manipulation and analysis.                                                                     |
| `python-dotenv` | `1.0.0`          | Management of environment variables.                                                                |
| `pandera`       | `0.19.0`         | Data validation for pandas dataframes.                                                              |
| `matplotlib`    | `3.10.6`         | Data visualization.                                                                                 |
| `pip-audit`     | `>=2.7.0, <4.2`  | Python dependency vulnerability scanning.                                                           |
| `pip`           | `>=25.2`         | The Python package installer.                                                                       |
| `setuptools`    | `80.9.0`         | **Security-critical.** Pinned to fix CVE-2024-6345 and CVE-2025-47273. Verified in the CI/CD pipeline. |
| `requests`      | `>=2.32.5`       | HTTP library.                                                                                       |
| `urllib3`       | `>=2.5.0`        | HTTP client.                                                                                        |
| `jinja2`        | `>=3.1.6`        | Templating engine.                                                                                  |
| `certifi`       | `>=2025.8.3`     | Root certificates for verifying the identity of TLS hosts.                                          |
| `cryptography`  | `>=46.0.2`       | Cryptographic recipes and primitives.                                                               |
| `idna`          | `>=3.10`         | Internationalized Domain Names in Applications (IDNA).                                              |
| `configobj`     | `>=5.0.9`        | Configuration file parser.                                                                          |

## 4. CI/CD and Security Scanning

The CI/CD pipeline automates testing, security scanning, and building the application.

-   **Python Dependency Scanning:**
    -   **Tool:** `pip-audit`
    -   **Configuration:** Scans all installed Python packages for known vulnerabilities.
    -   **Ignored Vulnerabilities:** The following vulnerabilities are explicitly ignored in the `pip-audit` scan. This was likely done after a risk assessment.
        -   `GHSA-4xh5-x5gv-qwph`
        -   `PYSEC-2024-75`
        -   `GHSA-c8m8-j448-xjx7`

-   **Docker Image Vulnerability Scanning:**
    -   **Tool:** `Trivy`
    -   **Action Version:** `aquasecurity/trivy-action@0.32.0`
    -   **Configuration:**
        -   Scans the Docker image for both OS and library vulnerabilities.
        -   Fails the build if `CRITICAL` or `HIGH` severity vulnerabilities are found.
        -   Ignores vulnerabilities that do not yet have a fix (`ignore-unfixed: true`).

-   **Build and Test:**
    -   **Testing:** `pytest` is used to run the test suite.
    -   **Docker Build:** The `docker/build-push-action@v5` action is used to build the Docker image, with caching enabled to speed up the process.