import mlflow
import mlflow.sklearn
import json
from datetime import datetime


class MLflowExperimentTracker:

    def __init__(self, experiment_name="InsightFlow-Experiments"):
        mlflow.set_experiment(experiment_name)
        self.experiment_name = experiment_name

    def start_run(self, run_name=None):

        if run_name is None:
            run_name = f"run_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}"

        return mlflow.start_run(run_name=run_name)

    def log_parameters(self, params: dict):

        for key, value in params.items():
            mlflow.log_param(key, value)

    def log_metrics(self, metrics: dict):

        for key, value in metrics.items():
            mlflow.log_metric(key, value)

    def log_model(self, model, artifact_path="model"):

        mlflow.sklearn.log_model(model, artifact_path)

    def log_artifact(self, file_path):

        mlflow.log_artifact(file_path)

    def end_run(self):

        mlflow.end_run()

    def register_model(self, model_uri, model_name):

        result = mlflow.register_model(model_uri, model_name)

        return result

    def get_experiment_runs(self):

        client = mlflow.tracking.MlflowClient()

        experiment = client.get_experiment_by_name(self.experiment_name)

        runs = client.search_runs(experiment_ids=[experiment.experiment_id])

        run_data = []

        for run in runs:
            run_data.append({
                "run_id": run.info.run_id,
                "status": run.info.status,
                "start_time": run.info.start_time,
                "metrics": run.data.metrics,
                "params": run.data.params
            })

        return run_data

    def save_experiment_report(self, path="experiments/experiment_report.json"):

        runs = self.get_experiment_runs()

        with open(path, "w") as f:
            json.dump(runs, f, indent=4)


if __name__ == "__main__":

    tracker = MLflowExperimentTracker()

    with tracker.start_run("demo_training"):

        tracker.log_parameters({
            "model": "IsolationForest",
            "dataset": "sales_data",
            "contamination": 0.05
        })

        tracker.log_metrics({
            "accuracy": 0.94,
            "f1_score": 0.91
        })

        tracker.end_run()

    tracker.save_experiment_report()

    print("Experiment report generated")