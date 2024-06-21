from kafka import KafkaConsumer
import json

# Configuration du consommateur Kafka
consumer = KafkaConsumer(
    'iot_data',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Consommer et imprimer les données
for message in consumer:
    print(f"Received message: {message.value}")
