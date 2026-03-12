from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from backend.database.db import Base


class Dataset(Base):

    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    description = Column(String, nullable=True)

    rows = Column(Integer)

    columns = Column(Integer)

    file_type = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)

    owner_id = Column(Integer, nullable=True)