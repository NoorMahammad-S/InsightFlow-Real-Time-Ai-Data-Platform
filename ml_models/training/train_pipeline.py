import pandas as pd
import mlflow

from ml_models.anomaly_detection.isolation_forest import AnomalyDetector
from ml_models.forecasting.prophet_model import SalesForecaster


class TrainingPipeline:

    def __init__(self):

        mlflow.set_experiment("InsightFlow-ML-Experiments")

        self.anomaly_model = AnomalyDetector()
        self.forecast_model = SalesForecaster()

    def load_data(self):

        df = pd.read_csv("data/sample_metrics.csv")

        return df

    def train_anomaly_model(self, df):

        features = [
            "sales_value",
            "sales_moving_avg",
            "sales_std_dev"
        ]

        with mlflow.start_run(run_name="anomaly_detection_training"):

            model = self.anomaly_model.train(df, features)

            mlflow.log_param("model", "IsolationForest")
            mlflow.log_param("features", features)

            self.anomaly_model.save_model()

            mlflow.log_artifact("models/anomaly_model.pkl")

            return model

    def train_forecasting_model(self, df):

        with mlflow.start_run(run_name="forecasting_training"):

            model = self.forecast_model.train(df)

            mlflow.log_param("model", "Prophet")

            self.forecast_model.save_model()

            mlflow.log_artifact("models/forecast_model.pkl")

            return model

    def run_pipeline(self):

        df = self.load_data()

        print("Training anomaly detection model...")
        self.train_anomaly_model(df)

        print("Training forecasting model...")
        self.train_forecasting_model(df)

        print("Training pipeline completed.")


if __name__ == "__main__":

    pipeline = TrainingPipeline()

    pipeline.run_pipeline()