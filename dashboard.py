import paho.mqtt.client as mqtt
import json

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print("Temperature:", data["temperature"], "°C")
    print("Humidity:", data["humidity"], "%")
    print("------------------------")

client = mqtt.Client()
client.on_message = on_message
client.connect("localhost", 1883)
client.subscribe("iot/weather")

client.loop_forever()
