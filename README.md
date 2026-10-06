# 🚀 Quiz Question Bank (B1-G6 DevOps Project)

[![CI/CD Pipeline](https://github.com/your-username/quiz-question-bank/actions/workflows/ci.yml/badge.svg)](https://github.com/your-username/quiz-question-bank/actions)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![Prometheus](https://img.shields.io/badge/Prometheus-Monitored-orange.svg)](https://prometheus.io/)
[![Grafana](https://img.shields.io/badge/Grafana-Visualized-F46800.svg)](https://grafana.com/)

An end-to-end DevOps practical project showcasing a modern, interactive **Quiz Question Bank** web application built with Flask, monitored with **Prometheus** & **Grafana**, containerized with **Docker**, orchestrated via **Docker Compose**, and automated through **GitHub Actions CI/CD**.

---

## 📌 Table of Contents
1. [System Architecture](#-system-architecture)
2. [DevOps Pipeline](#-devops-pipeline)
3. [Technology Stack](#-technology-stack)
4. [API Specification](#-api-specification)
5. [Local Development Setup](#-local-development-setup)
6. [Running Automated Tests](#-running-automated-tests)
7. [Docker Instructions](#-docker-instructions)
8. [Docker Compose Deployment](#-docker-compose-deployment)
9. [Prometheus Monitoring](#-prometheus-monitoring)
10. [Grafana Dashboard Setup](#-grafana-dashboard-setup)
11. [GitHub Actions CI/CD](#-github-actions-cicd)
12. [Submission Screenshot Checklist](#-submission-screenshot-checklist)

---

## 🏗 System Architecture

```text
                                 +--------------------+
                                 |    Web Browser     |
                                 |  (QuizBank UI SPA) |
                                 +---------+----------+
                                           | HTTP Requests
                                           v
                        +--------------------------------------+
                        |   quiz-question-bank (Port: 5000)    |
                        |         Flask REST API Engine        |
                        |   - GET /items       - POST /items   |
                        |   - GET /health      - GET /metrics  |
                        |      [In-Memory Question Bank]       |
                        +------------------+-------------------+
                                           | Scrapes /metrics
                                           v
                        +--------------------------------------+
                        |        Prometheus (Port: 9090)       |
                        |       Time-Series Metric Store       |
                        +------------------+-------------------+
                                           | Datasource Query
                                           v
                        +--------------------------------------+
                        |         Grafana (Port: 3000)         |
                        |       Real-time Visual Panels        |
                        +--------------------------------------+
```

---

## 🔄 DevOps Pipeline

```text
Jira (Task Tracker)
   └── Git / GitHub (Feature branch workflow)
         └── Pull Request & Code Review
               └── GitHub Actions (Automated pytest & Build)
                     └── Docker Hub (Container Registry)
                           └── Docker Compose (Multi-container orchestration)
                                 ├── Flask App Container
                                 ├── Prometheus Scraper
                                 └── Grafana Visualization
```

---

## 💻 Technology Stack

| Layer | Technologies Used |
|---|---|
| **Frontend** | Vanilla HTML5, Modern CSS3 (Glassmorphism & Variables), JavaScript ES6+ |
| **Backend** | Python 3.11 / 3.13, Flask, Werkzeug |
| **Monitoring** | Prometheus Client for Python, Prometheus Server, Grafana |
| **Testing** | pytest, Flask Test Client |
| **Containerization** | Docker, Docker Compose, Docker Hub |
| **CI/CD** | GitHub Actions |

---

## 🔌 API Specification

| Method | Endpoint | Description | Response Status |
|---|---|---|---|
| `GET` | `/` | Serves the interactive QuizBank Web Application | `200 OK` |
| `GET` | `/items` | Returns all quiz questions in memory | `200 OK` |
| `POST` | `/items` | Adds a new quiz question to memory | `201 Created` / `400 Bad Request` |
| `GET` | `/health` | API health check indicator (`{"status": "OK"}`) | `200 OK` |
| `GET` | `/metrics` | Prometheus metrics export | `200 OK` |

### Question Payload Schema (`POST /items`):
```json
{
  "question": "What is the primary role of CI/CD in DevOps?",
  "option_a": "Continuous Integration and Continuous Deployment automation",
  "option_b": "Replacing all unit tests with manual QA",
  "option_c": "Hardcoding secrets in repositories",
  "option_d": "Running single-node databases without backup",
  "answer": "A",
  "category": "DevOps",
  "difficulty": "Easy"
}
```

---

## ⚙️ Local Development Setup

### 1. Prerequisites
- Python 3.10+ installed
- Git installed

### 2. Setup Virtual Environment & Install Dependencies
```bash
# Clone the repository
git clone https://github.com/your-username/quiz-question-bank.git
cd quiz-question-bank

# Create and activate virtual environment
python -m venv venv
# On Windows (PowerShell):
venv\Scripts\Activate.ps1
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Start the Flask Server
```bash
python app.py
```
Open your browser at `http://localhost:5000` to view the QuizBank application.

---

## 🧪 Running Automated Tests

Run the full pytest suite:
```bash
pytest -v
```

Expected Output:
```text
============================= test session starts =============================
collected 7 items

test_app.py::test_health_check PASSED                                    [ 14%]
test_app.py::test_get_items PASSED                                       [ 28%]
test_app.py::test_post_item_success PASSED                               [ 42%]
test_app.py::test_post_item_missing_fields PASSED                        [ 57%]
test_app.py::test_post_item_invalid_answer PASSED                        [ 71%]
test_app.py::test_post_item_empty_payload PASSED                         [ 85%]
test_app.py::test_metrics_endpoint PASSED                                [100%]

============================== 7 passed in 0.27s ==============================
```

---

## 🐳 Docker Instructions

### 1. Build the Docker Image
```bash
docker build -t quiz-question-bank .
```

### 2. Run the Container
```bash
docker run -d -p 5000:5000 --name quiz-app quiz-question-bank
```

Access the application at `http://localhost:5000`.

### 3. Tag and Push to Docker Hub
```bash
# Log in to Docker Hub
docker login

# Tag the image
docker tag quiz-question-bank <dockerhub-username>/quiz-question-bank:latest

# Push the image
docker push <dockerhub-username>/quiz-question-bank:latest
```

---

## 🐙 Docker Compose Deployment

Run the complete multi-container stack (Flask App + Prometheus + Grafana) with a single command:

```bash
docker compose up -d --build
```

### Check Container Status
```bash
docker compose ps
```

| Service | Local URL | Default Credentials |
|---|---|---|
| **QuizBank App** | [http://localhost:5000](http://localhost:5000) | N/A |
| **Prometheus** | [http://localhost:9090](http://localhost:9090) | N/A |
| **Grafana** | [http://localhost:3000](http://localhost:3000) | `admin` / `admin` |

### Stop All Services
```bash
docker compose down
```

---

## 📈 Prometheus Monitoring

1. Open Prometheus at `http://localhost:9090`.
2. Navigate to **Status → Targets** and verify `quiz-question-bank:5000` is **UP**.
3. In the **Graph** tab, execute sample PromQL queries:
   - Total HTTP Requests: `flask_http_requests_total`
   - Request Rate (per sec): `rate(flask_http_requests_total[1m])`
   - Total Questions in Memory: `quizbank_questions_total`

---

## 📊 Grafana Dashboard Setup

1. Open Grafana at `http://localhost:3000` (Login: `admin` / `admin`).
2. Prometheus is automatically provisioned as the default datasource (`http://prometheus:9090`).
3. Click **+ → New Dashboard → Add visualization**.
4. Select **Prometheus** datasource.
5. Enter metric query:
   ```promql
   sum(rate(flask_http_requests_total[1m])) by (endpoint)
   ```
6. Set panel title to **Flask HTTP Request Rate by Endpoint** and click **Save**.

---

## 🐙 GitHub Actions CI/CD

The workflow `.github/workflows/ci.yml` triggers on any push or PR to `main`:
1. Checks out repository code.
2. Configures Python 3.11 environment.
3. Installs dependencies from `requirements.txt`.
4. Executes `pytest -v`.
5. On merge to `main`, builds Docker image and pushes to Docker Hub using secure GitHub Secrets (`DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN`).

---

## 📸 Submission Screenshot Checklist

For your Practical 10 submission, ensure you capture:
1. **GitHub Actions:** Green checkmark for CI pipeline run.
2. **Pytest Results:** Terminal showing `7 passed`.
3. **Frontend Dashboard:** QuizBank showing stats and question list.
4. **Interactive Quiz:** Question answer submission with green/red feedback & score tracker.
5. **API Health Check:** Browser / Postman showing `GET /health` -> `{"status": "OK"}`.
6. **Prometheus Targets:** `http://localhost:9090/targets` showing target state **UP**.
7. **Grafana Panel:** Real-time request graph populated from Flask traffic.
8. **Docker Hub:** Container image tagged and pushed to repository.
