# iot_producer.py
import json
import time
import random
from confluent_kafka import Producer
from kafka_config import KAFKA_PRODUCER_CONFIG

def delivery_report(err, msg):
    """ Fonction de retour d'appel exécutée une fois que le message a été livré ou une erreur a été signalée. """
    if err is not None:
        print(f'Erreur de livraison : {err}')
    else:
        print(f'Message livré à {msg.topic()} [{msg.partition()}]')

def send_iot_data(producer, topic):
    """ Fonction pour simuler l'envoi de données de capteurs IoT vers un topic Kafka donné. """
    while True:
        sensor_data = {
            'timestamp': int(time.time()),
            'sensor_id': 'sensor001',
            'temperature': round(random.uniform(20.0, 30.0), 2),
            'humidity': round(random.uniform(40.0, 60.0), 2)
        }
        
        producer.produce(topic, value=json.dumps(sensor_data).encode('utf-8'), callback=delivery_report)
        time.sleep(5)  # Simule l'envoi toutes les 5 secondes

        # Flusher le producer de temps en temps
        producer.flush()

def main():
    # Configuration du producteur Kafka (utilisation de la configuration partagée)
    producer = Producer(KAFKA_PRODUCER_CONFIG)

    # Envoyer des données de capteurs IoT à Kafka
    send_iot_data(producer, 'iot_data_topic')

if __name__ == '__main__':
    main()
