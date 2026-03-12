from fastapi import APIRouter

from backend.monitoring.ml_monitoring import (
    get_model_metrics,
    detect_data_drift
)

router = APIRouter(prefix="/monitoring", tags=["Monitoring"])


@router.get("/metrics")
def model_metrics():

    metrics = get_model_metrics()

    return metrics


@router.get("/drift")
def data_drift():

    drift = detect_data_drift()

    return {"drift_detected": drift}


@router.get("/health")
def system_health():

    return {
        "status": "healthy",
        "services": [
            "Kafka",
            "Spark",
            "Airflow",
            "MLflow",
            "FastAPI"
        ]
    }