import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest


def detect_anomalies(data: pd.DataFrame | None = None):

    """
    Detect anomalies in numerical data using Isolation Forest.
    """

    # If no data provided, create sample dataset
    if data is None:
        np.random.seed(42)
        normal_data = np.random.normal(50, 5, 100)
        anomaly_data = np.array([120, 130, 140])

        values = np.concatenate([normal_data, anomaly_data])

        data = pd.DataFrame({
            "value": values
        })

    model = IsolationForest(
        contamination=0.05,
        random_state=42
    )

    model.fit(data)

    predictions = model.predict(data)

    data["anomaly"] = predictions

    anomalies = data[data["anomaly"] == -1]

    return {
        "total_records": len(data),
        "anomalies_detected": len(anomalies),
        "anomaly_indices": anomalies.index.tolist()
    }