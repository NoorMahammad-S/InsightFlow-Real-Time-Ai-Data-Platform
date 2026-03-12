from datetime import timedelta
from feast import Entity, FeatureView, Field
from feast.types import Float32, Int64
from feast.data_source import FileSource


# ---------------------------------------------------------
# Data Source
# ---------------------------------------------------------

sales_data = FileSource(
    path="data/sales_features.parquet",
    event_timestamp_column="event_timestamp"
)


# ---------------------------------------------------------
# Entity Definition
# ---------------------------------------------------------

sales_entity = Entity(
    name="sales_id",
    value_type=Int64,
    description="Sales record identifier"
)


# ---------------------------------------------------------
# Feature View Definition
# ---------------------------------------------------------

sales_feature_view = FeatureView(
    name="sales_features",
    entities=[sales_entity],
    ttl=timedelta(days=1),
    schema=[
        Field(name="sales_value", dtype=Float32),
        Field(name="sales_moving_avg", dtype=Float32),
        Field(name="sales_std_dev", dtype=Float32),
    ],
    online=True,
    source=sales_data
)


# ---------------------------------------------------------
# Feature Service (optional grouping)
# ---------------------------------------------------------

from feast import FeatureService

sales_feature_service = FeatureService(
    name="sales_feature_service",
    features=[sales_feature_view]
)