from kafka import KafkaConsumer
from pymongo import MongoClient
import json

# Configuration Kafka
consumer = KafkaConsumer(
    'my_topic',                   # Nom du topic Kafka à consommer
    group_id='group_name',          # ID du groupe de consommateurs Kafka
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',   # Commencer à lire depuis le début du topic
    enable_auto_commit=True,        # Activer la validation automatique des offsets
    value_deserializer=lambda x: x.decode('utf-8')  # Désérialiser la valeur comme UTF-8 string
)

# Configuration MongoDB
try:
    client = MongoClient('localhost', 27017)
    db = client['mydatabase']       # Utilisation de la base de données 'mydatabase'
    collection = db['mycollection'] # Utilisation de la collection 'mycollection'
    print("Connected to MongoDB successfully!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit(1)

# Consommation et traitement des messages Kafka
for message in consumer:
    message_data = message.value
    payload ={ "data": message_data}
    try:
        # Désérialiser le JSON
        # payload = json.loads()
        print(payload)
        # Vérifier que payload est un dictionnaire
        if isinstance(payload, dict):
            # Insérer les données dans MongoDB
            collection.insert_one(payload)
            print(f"Message reçu et inséré dans MongoDB : {message_data}")
        else:
            print(f"Ignoring non-dictionary payload: {message_data}")
    except Exception as e:
        print(f"Error inserting into MongoDB: {e}")

# Fermeture du client MongoDB et du consommateur Kafka
client.close()
consumer.close()
