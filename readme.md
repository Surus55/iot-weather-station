Virtuális Hőmérséklet- és Páratartalom Mérő Eszköz - dr. Vántus Tamás (RGH95E)

Projekt leírása:

Ez a python projekt egy virtuális IoT eszközt mutat be, amely szimulál egy hőmérséklet- és páratartalom szenzort (DHT22), és az adatokat valós időben továbbítja egy dashboard felé az MQTT protokoll segítségével.


Architektúrája, működése:

Virtuális szenzor > MQTT Publisher (IoT eszköz) > Mosquitto Broker > Dashboard (felhasználói kliens)

- virtuális szenzor: szimulált véletlenszerű adatokat generál  
- publiher: elküldi az adatokat MQTT-n  
- broker: Mosquitto MQTT broker (!ezt előre telepíteni kell!)  
- dashboard: fogadja és megjeleníti az adatokat

Használt programok:
- Python 3.14  
- MQTT protokoll  
- Mosquitto MQTT Broker  
- "paho-mqtt" Python könyvtár  

Filok:
sensor_simulator.py - virtuális szenzor logika
mqtt_publisher.py - IoT eszköz, adatküldő
dashboard.py - adatfogadó és megjelenítő
run.bat - elindítja a publisher + dashboard

Telepítési útmutató:

1. Mosquitto MQTT Broker telepítése

2. Python telepítése

3. Szükséges Python csomag telepítése: paho-mqtt

A progi futtatása:

A projekt mappájában futtni kell a run.bat file-t, amely automatikusan elindítja a Mosquitto brokert (ha még nem fut), a Publishert (IoT eszköz) és a Dashboardot (adatfogadó) mindegyiket külön ablakban.

Működés leírása:

A virtuális szenzor 5 másodpercenként generál:
hőmérséklet adatokat (20–30 °C)
és páratartalom adatokat (40–70 %)
Az IoT eszköz (publisher) elküldi az adatokat MQTT-n a brokernek.
A dashboard valós időben fogadja és megjeleníti az adatokat.