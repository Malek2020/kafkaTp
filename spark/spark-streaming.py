from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pymongo import MongoClient
import json

# Configuration Kafka
kafka_params = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "spark-streaming-group",
    "auto.offset.reset": "earliest"
}

# Configuration MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['spark_results']

# Fonction pour sauvegarder dans MongoDB
def save_to_mongodb(rdd):
    for record in rdd.collect():
        message_data = json.loads(record[1])
        collection.insert_one(message_data)
        print(f"Message inséré dans MongoDB : {message_data}")

# Initialisation de SparkContext
sc = SparkContext(appName="SparkStreamingExample")
sc.setLogLevel("WARN")

# Initialisation de StreamingContext avec intervalle de 5 secondes
ssc = StreamingContext(sc, 5)

# Création du DStream
kafka_stream = KafkaUtils.createDirectStream(ssc, topics=["my_topic"], kafkaParams=kafka_params)

# Traitement du stream
processed_stream = kafka_stream.map(lambda x: (x[0], json.loads(x[1])))

# Calcul du nombre de messages par clé et sauvegarde dans MongoDB
key_counts = processed_stream.countByKey()
key_counts.foreachRDD(lambda rdd: save_to_mongodb(rdd))

# Démarrage du traitement en continu
ssc.start()
ssc.awaitTermination()
