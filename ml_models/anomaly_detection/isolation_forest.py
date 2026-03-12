import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest


class AnomalyDetector:

    def __init__(self, contamination=0.05):
        self.model = IsolationForest(
            contamination=contamination,
            random_state=42
        )

    def train(self, df: pd.DataFrame, feature_columns):
        """
        Train anomaly detection model
        """
        X = df[feature_columns]

        self.model.fit(X)

        return self.model

    def predict(self, df: pd.DataFrame, feature_columns):
        """
        Predict anomalies
        """
        X = df[feature_columns]

        predictions = self.model.predict(X)

        df["anomaly"] = predictions
        df["anomaly"] = df["anomaly"].apply(lambda x: 1 if x == -1 else 0)

        return df

    def save_model(self, path="models/anomaly_model.pkl"):
        joblib.dump(self.model, path)

    def load_model(self, path="models/anomaly_model.pkl"):
        self.model = joblib.load(path)
        return self.model


if __name__ == "__main__":

    data = pd.read_csv("data/sample_metrics.csv")

    features = ["sales_value", "sales_moving_avg", "sales_std_dev"]

    detector = AnomalyDetector()

    detector.train(data, features)

    results = detector.predict(data, features)

    print(results.head())