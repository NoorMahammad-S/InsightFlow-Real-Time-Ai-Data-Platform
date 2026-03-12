from fastapi import APIRouter, UploadFile, File
import pandas as pd
import io

from backend.services.ingestion_service import store_dataset

router = APIRouter(prefix="/datasets", tags=["Datasets"])


@router.post("/upload")
async def upload_dataset(file: UploadFile = File(...)):

    contents = await file.read()

    df = pd.read_csv(io.BytesIO(contents))

    store_dataset(df)

    return {"message": "Dataset uploaded successfully"}


@router.get("/")
def list_datasets():

    datasets = ["sales_2024.csv", "sales_2025.csv"]

    return {"datasets": datasets}