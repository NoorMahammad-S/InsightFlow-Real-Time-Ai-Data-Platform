import pandas as pd
import joblib
from prophet import Prophet


class SalesForecaster:

    def __init__(self):
        self.model = Prophet()

    def train(self, df: pd.DataFrame):
        """
        Train Prophet forecasting model
        """
        df = df.rename(columns={
            "event_timestamp": "ds",
            "sales_value": "y"
        })

        self.model.fit(df)

        return self.model

    def forecast(self, periods=30):

        future = self.model.make_future_dataframe(periods=periods)

        forecast = self.model.predict(future)

        return forecast

    def save_model(self, path="models/forecast_model.pkl"):
        joblib.dump(self.model, path)

    def load_model(self, path="models/forecast_model.pkl"):
        self.model = joblib.load(path)
        return self.model


if __name__ == "__main__":

    df = pd.read_csv("data/sales_timeseries.csv")

    forecaster = SalesForecaster()

    forecaster.train(df)

    forecast = forecaster.forecast()

    print(forecast.head())