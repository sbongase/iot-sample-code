import time, os
from signal import pause
import paho.mqtt.client as paho

def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

try:
    client = paho.Client()
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect("broker.mqttdashboard.com", 1883)
    client.subscribe("solan/subdata", qos=1)

    client.loop_forever()
except keyboardInterrupt:
        GPIO.cleanup()
