
# Project Status
This project is fully functional. All tests pass successfully in CI/CD and local environments.

# DevOps for Data: A CI/CD Pipeline for an Automated ETL Job

This project implements a complete Continuous Integration and Continuous Deployment (CI/CD) pipeline for a serverless ETL job. Using GitHub Actions, this pipeline automates the testing and packaging of data transformation code, ensuring that every change is validated before it can be deployed.

## 📋 Project Significance, Business Context & Results

The automated ETL pipeline from previous projects successfully solved data ingestion problems, but its development process remained manual. Any new code changes were deployed without automated testing, creating significant operational risk. A single faulty commit could break the entire data pipeline, leading to data delays, loss of trust, and emergency manual interventions.

This project addresses that risk by professionalizing the development lifecycle for data infrastructure. The solution applies DevOps principles (specifically CI/CD) to data engineering—a practice known as **DataOps**.

### Results & Outcomes
- All tests (unit, integration, data quality) pass in CI/CD and locally
- Automated gating for PRs and main branch merges
- Docker images are built and pushed to Docker Hub only after successful tests
- Data quality constraints are enforced on all ETL outputs
- Full reproducibility: pipeline can be cloned, tested, and deployed identically by any researcher

For expanded methodology, results, and reproducibility details, see the journal manuscript and `Case_Study.md`.

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

## 🛠️ Technologies Used & Expanded Features

| Technology           | Purpose                                      |
|----------------------|----------------------------------------------|
| Git & GitHub         | Version control and repository hosting       |
| GitHub Actions       | CI/CD platform for workflow automation       |
| Python               | Core language for the ETL application        |
| Pytest               | Framework for writing and running unit tests |
| Docker               | Containerization for reproducible environments |
| SQLite               | Database integration testing                 |
| Great Expectations   | Data quality validation                      |

### Expanded Pipeline Features
- **Database Integration Tests:** Validates ETL pipeline against SQLite for reproducibility and reliability.
- **Data Quality Tests:** Uses Great Expectations to enforce schema and value constraints on output data.
- **Branching & Workflow Strategy:** PRs require passing tests before merge; build job runs only after successful merges to main.

## 📁 Repository Structure (Expanded)
```
.
├── .github/
│   └── workflows/
│       └── ci-cd.yml # 🚀 CI/CD pipeline definition
├── src/
│   └── etl_pipeline/
│       ├── __init__.py
│       └── handler.py # 🐍 Main ETL application code
├── tests/
│   ├── __init__.py
│   ├── test_handler.py # ✅ Unit tests for ETL logic
│   ├── test_db_integration.py # 🗄️ Database integration tests
│   └── test_data_quality.py # 📊 Data quality tests
├── Dockerfile # 📦 Container blueprint
├── requirements.txt # 📜 Python dependencies
├── Case_Study.md # 🏢 Business context & scenario
└── README.md # 📖 This file
```

## ⚙️ Key Configuration Files & Reproducibility

- **`Dockerfile`**: Blueprint for building the container image
- **`.github/workflows/ci-cd.yml`**: Defines the entire CI/CD pipeline, including PR test enforcement and build gating
- **`requirements.txt`**: Lists all Python dependencies, including great_expectations for data quality
- **`tests/test_db_integration.py`**: Database integration tests for ETL reproducibility
- **`tests/test_data_quality.py`**: Data quality validation using Great Expectations


## 📊 How to Generate Figures
To generate the final publication-quality boxplot figure, run:

```bash
python generate_figures.py
```

This will save `boxplot_pipeline_durations.png` at 300 DPI in the project root.

## 🚀 How to Run the Pipeline & Reproduce Results

### Local Development & Reproducibility
1. **Clone the repository**:
   ```bash
   git clone https://github.com/JosephNjiru/dataops-cicd-pipeline-github-actions.git
   cd dataops-cicd-pipeline-github-actions
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run all tests locally**:
   ```bash
   pytest
   ```
4. **Build and run Docker image locally**:
   ```bash
   docker build -t dataops-pipeline .
   docker run --rm dataops-pipeline
   ```
