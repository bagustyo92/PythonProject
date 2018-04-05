import paho.mqtt.client as paho

def on_subscribe(client, userdata, mid, granted_qos):
    print("Node " + str(mid) + " SUBSCRIBED")

def on_message(client, userdata, msg):
    print("Data " + msg.topic + " : " + str(msg.payload))

client = paho.Client()
client.username_pw_set("admintes", "admin123")
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("139.59.225.39", 1883)

client.subscribe("data/sensor")