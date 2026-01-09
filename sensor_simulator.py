import random

def read_sensor():
    temperature = round(random.uniform(20, 30), 2)
    humidity = round(random.uniform(40, 70), 2)
    return temperature, humidity
