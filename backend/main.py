from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database.db import init_db

# API Routes
from backend.api.auth_routes import router as auth_router
from backend.api.dashboard_routes import router as dashboard_router
from backend.api.dataset_routes import router as dataset_router
from backend.api.monitoring_routes import router as monitoring_router


# -------------------------------------------------------
# FastAPI Application Initialization
# -------------------------------------------------------

app = FastAPI(
    title="InsightFlow AI Data Platform",
    description="Real-Time AI Data Platform for Analytics, Monitoring, and Forecasting",
    version="1.0.0"
)


# -------------------------------------------------------
# CORS Configuration
# -------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production specify frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------------------------------------
# Register API Routers
# -------------------------------------------------------

app.include_router(auth_router)
app.include_router(dashboard_router)
app.include_router(dataset_router)
app.include_router(monitoring_router)


# -------------------------------------------------------
# Startup Event
# -------------------------------------------------------

@app.on_event("startup")
def startup_event():
    """
    Initialize database and required resources
    """
    init_db()
    print("InsightFlow backend started successfully")


# -------------------------------------------------------
# Root Endpoint
# -------------------------------------------------------

@app.get("/")
def root():
    return {
        "platform": "InsightFlow",
        "description": "Real-Time AI Data Platform",
        "services": [
            "Authentication",
            "Dataset Ingestion",
            "Anomaly Detection",
            "Forecasting",
            "Monitoring"
        ],
        "status": "running"
    }


# -------------------------------------------------------
# Health Check Endpoint
# -------------------------------------------------------

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "services": {
            "api": "running",
            "database": "connected",
            "ml_models": "available"
        }
    }