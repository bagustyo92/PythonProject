import paho.mqtt.client as paho
import MySQLdb
import json

###sqldb Connect to database project
db = MySQLdb.connect("localhost", "bagus", "sql", "project")
cursor = db.cursor()
	

def on_subscribe(client, userdata, mid, granted_qos):
    print("STATUS : NODE " + str(mid) + " SUBSCRIBED")

def on_message(client, userdata, msg):
	print "Data " + msg.topic + " : " + str(msg.payload)

   	respon = json.loads(str(msg.payload))
	print "Your data : "
	print respon["sensor1"], respon["sensor2"], respon["sensor3"]
	data1 = respon["sensor1"]
	data2 = respon["sensor2"]
	data3 = respon["sensor3"]

	cetak = "INSERT INTO dataSensor VALUES (null, " + str(data1) + ", " + str(data2) + ", " + str(data3) + ", null)"
	cursor.execute(cetak)
	db.commit()

# def status(data1, data2, data3):
# 	#some formula here
# 	rumus = data1 + data2 + data3p
# 	return rumus

client = paho.Client()
client.username_pw_set("admintes", "admin123")
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("139.59.225.39", 1883)
#topic yang di publish rafi
client.subscribe("data/sensor")

client.loop_forever()
