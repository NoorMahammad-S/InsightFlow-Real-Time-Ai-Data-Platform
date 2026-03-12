from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.db import get_db
from backend.services.anomaly_service import detect_anomalies
from backend.services.forecasting_service import generate_forecast
from backend.analytics.spark_jobs.distributed_analytics import get_sales_summary

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/summary")
def dashboard_summary(db: Session = Depends(get_db)):

    analytics = get_sales_summary()

    anomalies = detect_anomalies()

    forecast = generate_forecast()

    return {
        "analytics": analytics,
        "anomalies": anomalies,
        "forecast": forecast
    }


@router.get("/sales")
def sales_data():

    data = get_sales_summary()

    return {"sales": data}