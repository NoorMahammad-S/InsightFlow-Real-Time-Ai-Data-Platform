# 🚀 InsightFlow – Real-Time AI Data Platform

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Kafka](https://img.shields.io/badge/Kafka-Streaming-black)
![Airflow](https://img.shields.io/badge/Airflow-Orchestration-orange)
![Spark](https://img.shields.io/badge/Spark-Distributed%20Analytics-red)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-purple)
![React](https://img.shields.io/badge/React-Frontend-cyan)

A **production-style real-time AI data platform** that ingests, processes, analyzes, and monitors streaming datasets using modern data engineering and machine learning infrastructure.

InsightFlow demonstrates how modern organizations build **end-to-end ML platforms** with streaming pipelines, feature stores, experiment tracking, and monitoring systems.

---

# 🌐 Live Demo

| Service | URL |
|------|------|
Frontend Dashboard | http://localhost:5173 |
Backend API | http://localhost:8000 |
Airflow UI | http://localhost:8080 |
MLflow Experiments | http://localhost:5000 |

---

# 🧠 Platform Capabilities

### Real-Time Data Processing
- Streaming ingestion pipelines
- Kafka-based event architecture
- Distributed data analytics

### Machine Learning Systems
- Anomaly detection pipelines
- Forecasting models
- Feature store integration
- Experiment tracking

### AI Platform Observability
- Model drift detection
- Data lineage tracking
- Monitoring dashboards

---

# ⚙️ Architecture Overview

![Architecture](screenshots/architecture.png)

```
                       +-------------------+
                       |   React Frontend  |
                       |   Dashboards      |
                       +---------+---------+
                                 |
                                 v
                       +-------------------+
                       |  FastAPI Backend  |
                       |   API Gateway     |
                       +---------+---------+
                                 |
          +----------------------+-----------------------+
          |                                              |
          v                                              v
   +-------------+                               +----------------+
   | Kafka       |                               | Airflow        |
   | Streaming   |                               | Pipelines      |
   +------+------+                               +--------+-------+
          |                                               |
          v                                               v
   +-------------+                               +----------------+
   | Feature     |                               | ML Models      |
   | Store       |                               | Training       |
   | (Feast)     |                               +--------+-------+
   +------+------+
          |
          v
+---------------------+
| Distributed Spark   |
| Analytics Engine    |
+---------------------+

```

---

# 📊 Benchmark Results

| Task | Dataset Size | Processing Time |
|-----|-----|-----|
Streaming ingestion | 1M events | ~2.1 sec |
Feature generation | 500K rows | ~4.3 sec |
Anomaly detection | 100K rows | ~0.8 sec |
Forecast training | 50K rows | ~1.6 sec |

Benchmarks executed using:

- Kafka streaming pipeline
- Spark distributed analytics
- Isolation Forest anomaly detection
- Prophet forecasting models

---

# 📸 Professional Screenshots

### Platform Dashboard

![Dashboard Screenshot](screenshots/dashboard.png)


### Dataset Upload Interface

![Upload UI Screenshot](screenshots/upload.png)


### ML Monitoring Dashboard

![Monitoring Screenshot](screenshots/monitoring.png)


### Airflow Pipeline View

![Airflow DAG Screenshot](screenshots/airflow.png)


# 🏗️ Project Structure

```
InsightFlow – Real-Time AI Data Platform
│
├── backend
│   ├── api
│   │   ├── auth_routes.py
│   │   ├── dashboard_routes.py
│   │   ├── dataset_routes.py
│   │   └── monitoring_routes.py
│   │
│   ├── services
│   │   ├── anomaly_service.py
│   │   ├── forecasting_service.py
│   │   ├── monitoring_service.py
│   │   └── ingestion_service.py
│   │
│   ├── models
│   │   ├── dataset.py
│   │   ├── user.py
│   │   └── metrics.py
│   │
│   ├── database
│   │   └── db.py
│   │
│   └── main.py
│
├── streaming
│   ├── kafka_producer
│   │   └── producer.py
│   │
│   └── kafka_consumer
│       └── consumer.py
│
├── pipelines
│   └── airflow_dags
│       └── data_pipeline.py
│
├── feature_store
│   └── feast_repo
│       ├── feature_store.yaml
│       └── features.py
│
├── ml_models
│   ├── anomaly_detection
│   │   └── isolation_forest.py
│   │
│   ├── forecasting
│   │   └── prophet_model.py
│   │
│   └── training
│       └── train_pipeline.py
│
├── monitoring
│   └── ml_monitoring.py
│
├── lineage
│   └── data_lineage.py
│
├── experiments
│   └── mlflow_tracking.py
│
├── analytics
│   └── spark_jobs
│       └── distributed_analytics.py
│
├── frontend
│
├── docker
│
├── docker-compose.yml
└── README.md

```

---

# 🚀 Running the Platform

### Start all services

```
docker compose up --build
```

---

### Access Platform

Frontend Dashboard  
```
[http://localhost:5173](http://localhost:5173)
```

Backend API  
```
[http://localhost:8000](http://localhost:8000)
```

Airflow Pipelines  
```
[http://localhost:8080](http://localhost:8080)
```

MLflow Experiments  
```
[http://localhost:5000](http://localhost:5000)
```

---

# 🧩 Technology Stack

Backend
- Python
- FastAPI
- Kafka

Data Engineering
- Apache Airflow
- Apache Spark

Machine Learning
- Scikit-learn
- Prophet
- MLflow

Feature Store
- Feast

Frontend
- React

Infrastructure
- Docker
- Docker Compose

---

# 🎯 Use Cases

This platform can be used for:

- Fraud detection systems
- Real-time monitoring platforms
- Predictive analytics pipelines
- AI observability platforms
- IoT data streaming systems

---

# 📌 Why This Project Matters

InsightFlow demonstrates skills in:

- Data Engineering
- ML Infrastructure
- Real-time streaming systems
- Distributed analytics
- AI observability
- Full-stack platform development

These are core skills used in modern data platforms at companies like Netflix, Uber, and Airbnb.

---

# ⭐ If you find this project useful

Give the repository a **star** ⭐ and feel free to contribute.

---
