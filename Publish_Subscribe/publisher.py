
"""
The Paho MQTT library is a Python client that implements the MQTT protocol, enabling communication
between devices in IoT applications through lightweight publish/subscribe messaging.
"""
import paho.mqtt.client as mqtt

from time import sleep

" MQTT broker details"
broker_ip="192.168.145.1"
port=1883
topic="home\led"
qos=0

" Create a new MQTT client"
client=mqtt.Client(client_id="Home")

" Connect to the broker"
client.connect(broker_ip,port)

while True:
    message="Led On"
    print(message)  #print for me
    "Publish message to the topic"
    client.publish(topic,message,qos)
    "Delay 2 seconds"
    sleep(2)

