import paho.mqtt.client as paho
import MySQLdb
import json

###sqldb Connect to database project
db = MySQLdb.connect("localhost", "bagus", "sql", "project")
cursor = db.cursor()
	

def on_subscribe(client, userdata, mid, granted_qos):
    print("Node " + str(mid) + " SUBSCRIBED")

def on_message(client, userdata, msg):
    print "Data " + msg.topic + " : " + str(msg.payload)

   	respon = json.dumps(json.loads('{"sensor1": 1, "sensor2": 37, "sensor3" : 70}'))
	print respon["sensor1"], respon["sensor2"], respon["sensor3"]
	data1 = respon["sensor1"]
	data2 = respon["sensor2"]
	data3 = respon["sensor3"]
    # except Exception as e:
    # 	print e

	##ragu disini karena extract dan ambil datanya gatau bener apa kaga
	# for id in resp:
	# 	print id["sensor1"], id["sensor2"], id["sensor3"]
	# 	data1 = id["sensor1"]
	# 	data2 = id["sensor2"]
	# 	data3 = id["sensor3"]

	# status = status()
	##ragu di fungsi str ini bener jadi string apa enggak trus bisa konek ke database ga
	cursor.execute("INSERT INTO dataSensor VALUES (null, " + data1 + ", " + data2 + ", " + data3 + ", null")


# def status(data1, data2, data3):
# 	#some formula here
# 	rumus = data1 + data2 + data3
# 	return rumus

client = paho.Client()
client.username_pw_set("admintes", "admin123")
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("139.59.225.39", 1883)
#topic yang di publish rafi
client.subscribe("data/sensor")

client.loop_forever()