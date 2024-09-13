
import paho.mqtt.client as mqtt

# MQTT broker details
broker_ip="192.168.145.1"
port=1883
topic="home\led"
qos=0

" Callback function for handling incoming messages"
def on_message(client, userdata, message):
    print(f"Recieved message : {message.payload.decode()}")

" Create an MQTT client "
client=mqtt.Client(client_id="Sub0")

" Assign the callback function (without calling it)"
client.on_message=on_message

# Connect to the broker
client.connect(broker_ip,port)

# Subscribe to the topic
client.subscribe(topic, qos)

client.loop_forever()
