# DevOps for Data: A CI/CD Pipeline for an Automated ETL Job

This project implements a complete Continuous Integration and Continuous Deployment (CI/CD) pipeline for a serverless ETL job. Using GitHub Actions, this pipeline automates the testing and packaging of data transformation code, ensuring that every change is validated before it can be deployed.

## 📋 Project Significance & Business Context

The automated ETL pipeline from previous projects successfully solved data ingestion problems, but its development process remained manual. Any new code changes were deployed without automated testing, creating significant operational risk. A single faulty commit could break the entire data pipeline, leading to data delays, loss of trust, and emergency manual interventions.

This project addresses that risk by professionalizing the development lifecycle for data infrastructure. The solution applies DevOps principles (specifically CI/CD) to data engineering—a practice known as **DataOps**.

The pipeline automates two critical stages:
- **Continuous Integration (CI)**: Automatically runs unit tests against every code change pushed to the main branch
- **Continuous Deployment (CD)**: Packages the application into a standardized Docker container for consistent deployment

## 🏗️ CI/CD Pipeline Architecture

The pipeline is orchestrated entirely within GitHub using GitHub Actions:
┌───────────────┐ ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐
│ Git Push to │ ───► │ GitHub Actions │ ───► │ Run Tests │ ───► │ Build Docker │
│ main Branch│ │ Trigger │ │ (pytest) │ │ Image │
└───────────────┘ └──────────────────┘ └──────────────────┘ └──────────────────┘

**Workflow Steps:**
1. **Trigger**: A developer pushes code to the main branch
2. **Test Job**: Sets up Python environment, installs dependencies, runs pytest test suite
3. **Build Job**: If tests pass, builds Docker image from Dockerfile
4. **Deployment Ready**: Produces a versioned, immutable artifact ready for deployment

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Git & GitHub | Version control and repository hosting |
| GitHub Actions | CI/CD platform for workflow automation |
| Python | Core language for the ETL application |
| Pytest | Framework for writing and running unit tests |
| Docker | Containerization for reproducible environments |

## 📁 Repository Structure
```
.
├── .github/
│ └── workflows/
│ └── ci-cd.yml # 🚀 CI/CD pipeline definition
├── src/
│ └── etl_pipeline/
│ ├── __init__.py
│ └── handler.py # 🐍 Main ETL application code
├── tests/
│ ├── __init__.py
│ └── test_handler.py # ✅ Unit tests for ETL logic
├── Dockerfile # 📦 Container blueprint
├── requirements.txt # 📜 Python dependencies
├── Case_Study.md # 🏢 Business context & scenario
└── README.md # 📖 This file
```

## ⚙️ Key Configuration Files

- **`Dockerfile`**: Blueprint for building the container image
- **`.github/workflows/ci-cd.yml`**: Defines the entire CI/CD pipeline
- **`requirements.txt`**: Lists all Python dependencies

## 🚀 How to Run the Pipeline

### Prerequisites
- A GitHub account
- Basic knowledge of Git, Python, and Docker
- (Optional) VS Code with Python and Docker extensions

### Local Development
1. **Clone the repository**:
   ```bash
   git clone https://github.com/JosephNjiru/dataops-cicd-pipeline-github-actions.git
   cd dataops-cicd-pipeline-github-actions
   ```
