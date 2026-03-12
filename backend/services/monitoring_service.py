import random
import psutil
import datetime


def get_system_metrics():

    """
    Collect system-level metrics.
    """

    metrics = {
        "cpu_usage_percent": psutil.cpu_percent(),
        "memory_usage_percent": psutil.virtual_memory().percent,
        "disk_usage_percent": psutil.disk_usage("/").percent,
        "timestamp": datetime.datetime.utcnow().isoformat()
    }

    return metrics


def get_model_performance():

    """
    Simulated ML model performance metrics.
    """

    performance = {
        "model_name": "sales_forecasting_model",
        "accuracy": round(random.uniform(0.85, 0.95), 3),
        "precision": round(random.uniform(0.82, 0.94), 3),
        "recall": round(random.uniform(0.80, 0.93), 3),
        "f1_score": round(random.uniform(0.82, 0.94), 3)
    }

    return performance


def monitoring_summary():

    """
    Combined monitoring summary.
    """

    return {
        "system_metrics": get_system_metrics(),
        "model_performance": get_model_performance()
    }