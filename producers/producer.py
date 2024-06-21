from confluent_kafka import Producer
import json
import time
import uuid

def delivery_report(err, msg):
    """ Fonction de retour d'appel exécutée une fois que le message a été livré ou une erreur a été signalée. """
    if err is not None:
        print(f'Erreur de livraison : {err}')
    else:
        print(f'Message livré à {msg.topic()} [{msg.partition()}]')

def send_messages(producer, topic, messages):
    """ Fonction pour envoyer une liste de messages à un topic Kafka donné. """
    for message in messages:
        producer.produce(topic, key=message[0], value=message[1].encode('utf-8'), callback=delivery_report)
    producer.flush()

def main():
    # Configuration du producteur Kafka
    conf = {
        'bootstrap.servers': 'localhost:9092',
        'client.id': 'python-producer',
        'queue.buffering.max.messages': 10000,   # Nombre maximal de messages en mémoire avant l'envoi à Kafka
        'queue.buffering.max.ms': 1000           # Délai maximal d'attente en millisecondes avant l'envoi à Kafka
    }
    
    producer = Producer(conf)

    # Envoyer plusieurs messages avec différentes clés et valeurs
    messages = [
        ('key1', 'Message 1'),
        ('key2', 'Message 2'),
        ('key3', 'Message 3')
    ]
    send_messages(producer, 'my_topic', messages)

    # Simulation de logs web
    while True:
        log_data = {
            'timestamp': int(time.time()),
            'ip_address': '192.168.1.1',
            'request': 'GET /index.html HTTP/1.1',
            'response_code': 200
        }

        # Envoi asynchrone des logs à Kafka
        producer.produce('web_logs_topic', value=json.dumps(log_data).encode('utf-8'), callback=delivery_report)
        time.sleep(1)  # Simule une nouvelle entrée de log toutes les secondes
    
    producer.flush()

if __name__ == '__main__':
    main()
