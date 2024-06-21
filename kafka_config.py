# kafka_config.py

KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'
KAFKA_CLIENT_ID = 'python-producer'

KAFKA_PRODUCER_CONFIG = {
    'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
    'client.id': KAFKA_CLIENT_ID,
    'security.protocol': 'PLAINTEXT',   # Exemple de configuration de sécurité
    'acks': 'all',                      # Exemple de configuration d'accusé de réception
    'queue.buffering.max.messages': 10000,
    'queue.buffering.max.ms': 1000
    # Ajoutez d'autres configurations Kafka nécessaires ici
}
