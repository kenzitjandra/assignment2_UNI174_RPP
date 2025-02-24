from flask import Flask, jsonify, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime

app = Flask(__name__)

# Koneksi ke MongoDB
uri = "mongodb+srv://rpp:rpp12345@rpp.jtumn.mongodb.net/?retryWrites=true&w=majority&appName=RPP"
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Pilih database
# db = client['MyDatabase']
# my_collection = db['SensorData']

# db = client['SensorDatabase']
# my_collection = db['DataSensor']

db = client['SensorDatabase1']
my_collection = db['DataSensor1']

# Menyimpan data ke MongoDB
def store_data(data):
    result = my_collection.insert_one(data)
    return result.inserted_id


def get_data():
    data = my_collection.find()
    return data

# @app.route('/', methods=['GET'])
# def entry_point():
#      return jsonify(message = "Hello World")

# Endpoint untuk menyimpan data sensor
@app.route('/sensor', methods=['POST'])
def store_sensor_data():
    try:
        body = request.get_json()

        temperature = body.get('temperature', 0)
        humidity = body.get('humidity', 0)
        motion = body.get('motion', 0)
        led = body.get('led', 0)

        data_to_store = {
            "temperature": temperature,
            "humidity": humidity,
            "motion": motion,
            "led": led,
            "timestamp": datetime.utcnow()
        }

        store_data(data_to_store)  # Simpan ke MongoDB

        return jsonify({"message": "✅ Data stored successfully!"}), 201

    except Exception as e:  # ⬅ Sejajarkan `except` dengan `try`
        return jsonify({"error": str(e)}), 500

# Endpoint untuk mengambil semua data sensor dari MongoDB
@app.route('/sensor', methods=['GET'])
def get_sensor_data():
    try:
        # Ambil semua data dari MongoDB dan konversi ke list
        data = list(sensor_collection.find({}, {"_id": 0}))  # Hapus _id agar tidak dikirim ke client

        return jsonify({"message": "✅ Data retrieved successfully!", "data": data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
# host='0.0.0.0', port=5000, 