# Projet Kafka : Traitement en Temps Réel et Intégration avec des Bases de Données NoSQL

Ce projet utilise Apache Kafka pour la gestion de flux de données en temps réel. Nous avons développé des producteurs de données simulées ainsi que des consommateurs pour traiter ces données et les intégrer avec des bases de données NoSQL comme Apache Cassandra ou MongoDB.

## Configuration de l'Environnement

### Prérequis
- Docker installé sur votre machine.
- Clonez ce dépôt GitHub : `<lien-vers-votre-repository>`

### Installation de Kafka
Pour exécuter Apache Kafka à l'aide de Docker Compose, utilisez la commande suivante :
```bash
docker-compose up -d

# Producteurs de Données
##Producteur de Transactions Financières
Description :
Le script financial_producer.py envoie des données de transactions financières simulées vers le topic financial_transactions_topic.

Utilisation :
Exécutez le producteur avec Python :
python financial_producer.py
##2. Producteur de Données de Capteurs IoT
Description :
Le script iot_producer.py envoie des données de capteurs IoT simulées vers le topic iot_data_topic.

Utilisation :
Exécutez le producteur avec Python :

python iot_producer.py

### Consommation des messages de financial_transactions_topic :

docker run --rm --net=host confluentinc/cp-kafka kafka-console-consumer --topic financial_transactions_topic --from-beginning --bootstrap-server localhost:9092
### Consommation des messages de iot_data_topic :

docker run --rm --net=host confluentinc/cp-kafka kafka-console-consumer --topic iot_data_topic --from-beginning --bootstrap-server localhost:9092
### Consommation des messages de my_topic :

docker run --rm --net=host confluentinc/cp-kafka kafka-console-consumer --topic my_topic --from-beginning --bootstrap-server localhost:9092
### Consommation des messages de web_logs_topic :
docker run --rm --net=host confluentinc/cp-kafka kafka-console-consumer --topic web_logs_topic --from-beginning --bootstrap-server localhost:9092

