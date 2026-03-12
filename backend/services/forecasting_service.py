import pandas as pd
import numpy as np
from prophet import Prophet


def generate_forecast():

    """
    Generate time-series forecast for demo sales data.
    """

    # Create sample time series data
    dates = pd.date_range(start="2024-01-01", periods=120)

    sales = np.random.randint(100, 500, 120)

    df = pd.DataFrame({
        "ds": dates,
        "y": sales
    })

    model = Prophet()

    model.fit(df)

    future = model.make_future_dataframe(periods=30)

    forecast = model.predict(future)

    result = forecast[["ds", "yhat"]].tail(30)

    return result.to_dict(orient="records")