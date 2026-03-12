import pandas as pd
from sqlalchemy.orm import Session
from backend.database.db import SessionLocal
from backend.models.dataset import Dataset


def store_dataset(df: pd.DataFrame):

    """
    Store dataset metadata in database.
    """

    db: Session = SessionLocal()

    dataset_record = Dataset(
        name="uploaded_dataset",
        rows=len(df),
        columns=len(df.columns)
    )

    db.add(dataset_record)
    db.commit()
    db.close()

    return True


def ingest_csv(file_path: str):

    """
    Load CSV file into DataFrame.
    """

    df = pd.read_csv(file_path)

    store_dataset(df)

    return df


def ingest_excel(file_path: str):

    """
    Load Excel file into DataFrame.
    """

    df = pd.read_excel(file_path)

    store_dataset(df)

    return df


def dataset_statistics(df: pd.DataFrame):

    """
    Generate basic statistics for dataset.
    """

    stats = {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "column_types": df.dtypes.astype(str).to_dict()
    }

    return stats