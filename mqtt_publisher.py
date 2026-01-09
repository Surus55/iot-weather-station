import paho.mqtt.client as mqtt
import json, time
from sensor_simulator import read_sensor

client = mqtt.Client()
client.connect("localhost", 1883)

while True:
    temp, hum = read_sensor()
    data = {
        "temperature": temp,
        "humidity": hum
    }
    client.publish("iot/weather", json.dumps(data))
    print("Sent:", data)
    time.sleep(5)
