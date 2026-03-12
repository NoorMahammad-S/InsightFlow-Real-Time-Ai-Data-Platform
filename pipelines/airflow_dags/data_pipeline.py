from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

import pandas as pd
import numpy as np


# ---------------------------------------------------------
# Default DAG Arguments
# ---------------------------------------------------------

default_args = {
    "owner": "insightflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}


# ---------------------------------------------------------
# DAG Definition
# ---------------------------------------------------------

dag = DAG(
    dag_id="insightflow_data_pipeline",
    default_args=default_args,
    description="End-to-End Data Pipeline for InsightFlow AI Platform",
    schedule_interval="@daily",
    catchup=False
)


# ---------------------------------------------------------
# Task 1: Data Ingestion
# ---------------------------------------------------------

def ingest_data():

    print("Starting data ingestion...")

    # Simulated dataset
    df = pd.DataFrame({
        "timestamp": pd.date_range(start="2024-01-01", periods=100),
        "sales": np.random.randint(50, 500, 100)
    })

    df.to_csv("/tmp/insightflow_dataset.csv", index=False)

    print("Dataset stored at /tmp/insightflow_dataset.csv")


ingestion_task = PythonOperator(
    task_id="data_ingestion",
    python_callable=ingest_data,
    dag=dag
)


# ---------------------------------------------------------
# Task 2: Feature Engineering
# ---------------------------------------------------------

def feature_engineering():

    print("Starting feature engineering...")

    df = pd.read_csv("/tmp/insightflow_dataset.csv")

    df["sales_moving_avg"] = df["sales"].rolling(window=5).mean()

    df["sales_std"] = df["sales"].rolling(window=5).std()

    df.to_csv("/tmp/insightflow_features.csv", index=False)

    print("Feature dataset saved")


feature_task = PythonOperator(
    task_id="feature_engineering",
    python_callable=feature_engineering,
    dag=dag
)


# ---------------------------------------------------------
# Task 3: Model Training
# ---------------------------------------------------------

def train_model():

    print("Training ML model...")

    df = pd.read_csv("/tmp/insightflow_features.csv")

    avg_sales = df["sales"].mean()

    print("Model trained. Avg sales:", avg_sales)


training_task = PythonOperator(
    task_id="train_model",
    python_callable=train_model,
    dag=dag
)


# ---------------------------------------------------------
# Task 4: Anomaly Detection
# ---------------------------------------------------------

def detect_anomalies():

    print("Running anomaly detection...")

    df = pd.read_csv("/tmp/insightflow_features.csv")

    threshold = df["sales"].mean() + 2 * df["sales"].std()

    anomalies = df[df["sales"] > threshold]

    print("Anomalies detected:", len(anomalies))


anomaly_task = PythonOperator(
    task_id="anomaly_detection",
    python_callable=detect_anomalies,
    dag=dag
)


# ---------------------------------------------------------
# Task 5: Forecasting
# ---------------------------------------------------------

def run_forecasting():

    print("Running forecasting pipeline...")

    df = pd.read_csv("/tmp/insightflow_features.csv")

    last_value = df["sales"].iloc[-1]

    forecast = [last_value + np.random.randint(-20, 20) for _ in range(7)]

    print("7-day forecast:", forecast)


forecast_task = PythonOperator(
    task_id="forecasting",
    python_callable=run_forecasting,
    dag=dag
)


# ---------------------------------------------------------
# DAG Task Order
# ---------------------------------------------------------

ingestion_task >> feature_task >> training_task >> anomaly_task >> forecast_task