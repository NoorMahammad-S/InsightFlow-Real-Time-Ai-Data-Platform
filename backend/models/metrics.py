from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from backend.database.db import Base


class ModelMetrics(Base):

    __tablename__ = "model_metrics"

    id = Column(Integer, primary_key=True, index=True)

    model_name = Column(String, nullable=False)

    version = Column(String)

    accuracy = Column(Float)

    precision = Column(Float)

    recall = Column(Float)

    f1_score = Column(Float)

    dataset_used = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)