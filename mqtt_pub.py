import time, os
from signal import pause
import paho.mqtt.client as paho

def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

client = paho.Client()
client.on_publish = on_publish
client.on_connect = on_connect
client.connect("broker.mqttdashboard.com", 1883)
client.loop_start()

while True:
    data_string = "off"
    print("button_state: "+data_string)
    (rc, mid) = client.publish("solan/pubdata", data_string, qos=1)
    time.sleep(5)

client.loop_stop()
