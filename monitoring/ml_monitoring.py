import pandas as pd
import numpy as np
import json
import time
from datetime import datetime


class MLMonitoring:

    def __init__(self):
        self.metrics_history = []

    def calculate_data_drift(self, reference_df: pd.DataFrame, new_df: pd.DataFrame, feature_columns):
        """
        Detect drift between reference dataset and new incoming dataset
        """

        drift_report = {}

        for col in feature_columns:

            ref_mean = reference_df[col].mean()
            new_mean = new_df[col].mean()

            ref_std = reference_df[col].std()
            new_std = new_df[col].std()

            mean_shift = abs(new_mean - ref_mean)

            drift_report[col] = {
                "reference_mean": ref_mean,
                "new_mean": new_mean,
                "mean_shift": mean_shift,
                "reference_std": ref_std,
                "new_std": new_std
            }

        return drift_report

    def prediction_monitoring(self, predictions):

        predictions = np.array(predictions)

        metrics = {
            "timestamp": str(datetime.utcnow()),
            "prediction_mean": float(np.mean(predictions)),
            "prediction_std": float(np.std(predictions)),
            "prediction_min": float(np.min(predictions)),
            "prediction_max": float(np.max(predictions)),
        }

        self.metrics_history.append(metrics)

        return metrics

    def anomaly_rate(self, predictions):

        predictions = np.array(predictions)

        anomalies = np.sum(predictions == 1)

        rate = anomalies / len(predictions)

        return {
            "anomaly_count": int(anomalies),
            "total_predictions": int(len(predictions)),
            "anomaly_rate": float(rate)
        }

    def save_monitoring_report(self, report, path="monitoring/report.json"):

        with open(path, "w") as f:
            json.dump(report, f, indent=4)

    def generate_monitoring_summary(self):

        if not self.metrics_history:
            return {"message": "No monitoring data available"}

        df = pd.DataFrame(self.metrics_history)

        summary = {
            "avg_prediction_mean": df["prediction_mean"].mean(),
            "avg_prediction_std": df["prediction_std"].mean(),
            "total_runs": len(df)
        }

        return summary


if __name__ == "__main__":

    monitor = MLMonitoring()

    reference = pd.DataFrame({
        "sales_value": np.random.normal(100, 10, 1000),
        "sales_moving_avg": np.random.normal(95, 5, 1000),
        "sales_std_dev": np.random.normal(3, 1, 1000)
    })

    new_data = pd.DataFrame({
        "sales_value": np.random.normal(110, 15, 1000),
        "sales_moving_avg": np.random.normal(98, 6, 1000),
        "sales_std_dev": np.random.normal(4, 1.2, 1000)
    })

    drift = monitor.calculate_data_drift(
        reference,
        new_data,
        ["sales_value", "sales_moving_avg", "sales_std_dev"]
    )

    print("Drift Report:", drift)