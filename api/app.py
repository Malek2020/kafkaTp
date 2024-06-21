from flask import Flask, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app)  # Active CORS pour toutes les routes

# Configuration MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
mongo = PyMongo(app)

# Route pour récupérer les données du tableau de bord
@app.route('/api/dashboard', methods=['GET'])
def get_dashboard_data():
    try:
        # dashboard_data = list(mongo.db['mycollection'].find())
        dashboard_data = []
        cursor = mongo.db['mycollection'].find({})
        for event in cursor:
            del event["_id"]
            dashboard_data.append(event)
        return jsonify(dashboard_data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
