import json
from kafka import KafkaConsumer


# ------------------------------------------------------
# Kafka Configuration
# ------------------------------------------------------

KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "insightflow_events"


# ------------------------------------------------------
# Kafka Consumer Initialization
# ------------------------------------------------------

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="insightflow-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)


# ------------------------------------------------------
# Process Incoming Events
# ------------------------------------------------------

def process_event(event):

    print("Received event:", event)

    # Example: detect anomaly
    value = event.get("value", 0)

    if value > 450:
        print("⚠ Potential anomaly detected:", value)


# ------------------------------------------------------
# Start Consumer
# ------------------------------------------------------

def start_consumer():

    print("Starting Kafka consumer...")

    for message in consumer:

        event = message.value

        process_event(event)


# ------------------------------------------------------
# Run Consumer
# ------------------------------------------------------

if __name__ == "__main__":
    start_consumer()