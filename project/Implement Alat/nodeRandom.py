import paho.mqtt.client as paho
import sys, datetime, time, json
from random import randint

counter = 0

def sensorAsap():
	sensor = randint(30,800)
	return sensor

def sensorSulfur():
	sensor = randint(50,3000)
	return sensor

def sensorKarbon():
	sensor = randint(1,70)
	return sensor

def sensorOzon():
	sensor = randint(100,2000)
	return sensor

def sensorNitrogen():
	sensor = randint(200,4000)
	return sensor

client = paho.Client()
client.username_pw_set("admintes", "admin123")
client.connect("ngehubx.online", 1883)

client.loop_start()
while True :
	#=== MESSAGE TO PUBLISH ===
	ts = time.time()
	waktu = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
	counter=counter + 1
	#Fotmat JSON
	kirim = {'id': counter, 'asap': sensorAsap(), 'karbon': sensorKarbon(), 'timestamp': str(waktu)}
	# kirim = {'id': counter, 'asap': 20, 'nitrogen' : 15, 'sulfur': 10, 'karbon': 21, 'ozon': 14, 'timestamp': str(waktu)}
	pesan = json.dumps(kirim)
	message = pesan
	print message
	client.publish("project/dataSensor", message)
	time.sleep(3)