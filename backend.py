
import paho.mqtt.client as mqtt
import pymongo
import json
from datetime import datetime
import time

conn = pymongo.MongoClient('mongodb://localhost:27017')
db = conn.TestingMqtt

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode()))
    Temp = json.loads(message.payload.decode())['temp']
    Organization = json.loads(message.payload.decode())['org']
    Device_ID = json.loads(message.payload.decode())['d_id']
    Freeze_ID = json.loads(message.payload.decode())['f_id']
    print("Info", Temp, Organization, Device_ID, Freeze_ID)

    collections = db.list_collection_names()
    list = []
    if Organization not in collections:
        db.create_collection(Organization)

    list.append({
        "metadata": {"device_name": Device_ID, "freeze_id": Freeze_ID, "type": "temperature"},
        "timestamp": datetime.today().replace(microsecond=0),
        "temp": Temp,
    })
    db[Organization].insert_many(list)

mqttbroker = "10.10.5.82"
port = 1883
client = mqtt.Client("P1")
client.connect(mqttbroker, port)

client.subscribe("#")
client.on_message = on_message
time.sleep(1)

client.loop_forever()


    
