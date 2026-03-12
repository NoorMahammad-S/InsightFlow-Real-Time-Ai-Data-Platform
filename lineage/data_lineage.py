import json
from datetime import datetime


class DataLineageTracker:

    def __init__(self):
        self.lineage_records = []

    def log_dataset_ingestion(self, dataset_name, source, record_count):

        record = {
            "event": "dataset_ingestion",
            "dataset_name": dataset_name,
            "source": source,
            "record_count": record_count,
            "timestamp": str(datetime.utcnow())
        }

        self.lineage_records.append(record)

        return record

    def log_transformation(self, dataset_name, transformation):

        record = {
            "event": "data_transformation",
            "dataset_name": dataset_name,
            "transformation": transformation,
            "timestamp": str(datetime.utcnow())
        }

        self.lineage_records.append(record)

        return record

    def log_feature_generation(self, feature_name, source_dataset):

        record = {
            "event": "feature_generation",
            "feature_name": feature_name,
            "source_dataset": source_dataset,
            "timestamp": str(datetime.utcnow())
        }

        self.lineage_records.append(record)

        return record

    def log_model_training(self, model_name, dataset_name):

        record = {
            "event": "model_training",
            "model_name": model_name,
            "dataset_name": dataset_name,
            "timestamp": str(datetime.utcnow())
        }

        self.lineage_records.append(record)

        return record

    def log_model_prediction(self, model_name, input_dataset):

        record = {
            "event": "model_prediction",
            "model_name": model_name,
            "input_dataset": input_dataset,
            "timestamp": str(datetime.utcnow())
        }

        self.lineage_records.append(record)

        return record

    def get_lineage_history(self):

        return self.lineage_records

    def save_lineage(self, path="lineage/lineage_log.json"):

        with open(path, "w") as f:
            json.dump(self.lineage_records, f, indent=4)


if __name__ == "__main__":

    lineage = DataLineageTracker()

    lineage.log_dataset_ingestion(
        dataset_name="sales_data",
        source="csv_upload",
        record_count=10000
    )

    lineage.log_transformation(
        dataset_name="sales_data",
        transformation="calculate moving average"
    )

    lineage.log_feature_generation(
        feature_name="sales_moving_avg",
        source_dataset="sales_data"
    )

    lineage.log_model_training(
        model_name="IsolationForest",
        dataset_name="sales_data"
    )

    lineage.log_model_prediction(
        model_name="IsolationForest",
        input_dataset="streaming_sales_data"
    )

    lineage.save_lineage()

    print(lineage.get_lineage_history())