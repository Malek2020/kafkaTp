# financial_producer.py
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

def send_financial_transactions(producer, topic):
    """ Fonction pour simuler l'envoi de transactions financières vers un topic Kafka donné. """
    while True:
        transaction_data = {
            'timestamp': int(time.time()),
            'account_from': 'account001',
            'account_to': 'account002',
            'amount': round(random.uniform(100.0, 1000.0), 2)
        }
        
        producer.produce(topic, value=json.dumps(transaction_data).encode('utf-8'), callback=delivery_report)
        time.sleep(10)  # Simule l'envoi toutes les 10 secondes

        # Flusher le producer de temps en temps
        producer.flush()

def main():
    conf = {'bootstrap.servers': 'localhost:9092',
            'client.id': 'error-handling-producer'}
    
    # Configuration du producteur Kafka (utilisation de la configuration partagée)
    producer = Producer(conf)

    # Exemple d'envoi de message susceptible d'échouer
    try:
        producer.produce('my_topic', value='Message important'.encode('utf-8'), callback=delivery_report)
        producer.flush()
    except Exception as e:
        print(f'Erreur lors de l\'envoi du message : {e}')
        # Ici, vous pouvez ajouter la logique de gestion d'erreurs
        
    # Envoyer des transactions financières à Kafka
    send_financial_transactions(producer, 'financial_transactions_topic')

if __name__ == '__main__':
    main()
