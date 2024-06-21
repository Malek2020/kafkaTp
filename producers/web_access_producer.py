# web_access_producer.py
import json
import time
from faker import Faker
from confluent_kafka import Producer
from kafka_config import KAFKA_PRODUCER_CONFIG

fake = Faker()

def delivery_report(err, msg):
    if err is not None:
        print(f'Erreur de livraison : {err}')
    else:
        print(f'Message livré à {msg.topic()} [{msg.partition()}]')

def main():
    producer = Producer(KAFKA_PRODUCER_CONFIG)
    while True:
        web_access_data = {
            'timestamp': int(time.time()),
            'user_id': fake.user_name(),   # Nom d'utilisateur généré aléatoirement
            'request_url': fake.uri(),     # URL générée aléatoirement
            'ip_address': fake.ipv4(),     # Adresse IP générée aléatoirement
            'response_time_ms': round(random.uniform(10.0, 500.0), 2)  # Temps de réponse aléatoire entre 10.0 et 500.0 ms
        }
        producer.produce('web_access_logs', value=json.dumps(web_access_data).encode('utf-8'), callback=delivery_report)
        time.sleep(5)  # Envoi toutes les 5 secondes

        producer.flush()

if __name__ == '__main__':
    main()
