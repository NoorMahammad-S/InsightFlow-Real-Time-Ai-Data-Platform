from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, stddev, sum as spark_sum


class DistributedAnalytics:

    def __init__(self, app_name="InsightFlow-Analytics"):

        self.spark = SparkSession.builder \
            .appName(app_name) \
            .getOrCreate()

    def load_dataset(self, path):

        df = self.spark.read.csv(path, header=True, inferSchema=True)

        return df

    def sales_summary(self, df):

        summary = df.select(
            avg(col("sales_value")).alias("avg_sales"),
            stddev(col("sales_value")).alias("sales_std"),
            spark_sum(col("sales_value")).alias("total_sales")
        )

        return summary

    def category_analysis(self, df):

        result = df.groupBy("product_category") \
            .sum("sales_value") \
            .withColumnRenamed("sum(sales_value)", "category_sales")

        return result

    def anomaly_analysis(self, df):

        anomalies = df.filter(col("anomaly") == 1)

        count = anomalies.count()

        return {
            "total_anomalies": count
        }

    def save_results(self, df, path):

        df.write.mode("overwrite").csv(path, header=True)

    def run_full_analytics_pipeline(self, dataset_path):

        print("Loading dataset...")

        df = self.load_dataset(dataset_path)

        print("Computing sales summary...")

        summary = self.sales_summary(df)

        summary.show()

        print("Running category analysis...")

        category = self.category_analysis(df)

        category.show()

        print("Running anomaly analysis...")

        anomaly_stats = self.anomaly_analysis(df)

        print(anomaly_stats)

        print("Analytics pipeline completed")

    def stop(self):

        self.spark.stop()


if __name__ == "__main__":

    analytics = DistributedAnalytics()

    analytics.run_full_analytics_pipeline("data/sales_dataset.csv")

    analytics.stop()