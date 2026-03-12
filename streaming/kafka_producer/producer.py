import json
import time
import random
from kafka import KafkaProducer
from datetime import datetime


# ------------------------------------------------------
# Kafka Configuration
# ------------------------------------------------------

KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "insightflow_events"


# ------------------------------------------------------
# Kafka Producer Initialization
# ------------------------------------------------------

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)


# ------------------------------------------------------
# Generate Streaming Data
# ------------------------------------------------------

def generate_event():

    event = {
        "event_id": random.randint(1000, 9999),
        "dataset": "sales_data",
        "value": random.randint(50, 500),
        "timestamp": datetime.utcnow().isoformat()
    }

    return event


# ------------------------------------------------------
# Stream Data to Kafka
# ------------------------------------------------------

def stream_events():

    print("Starting Kafka producer...")

    while True:

        event = generate_event()

        producer.send(TOPIC_NAME, event)

        print("Event sent:", event)

        time.sleep(2)


# ------------------------------------------------------
# Run Producer
# ------------------------------------------------------

if __name__ == "__main__":
    stream_events()