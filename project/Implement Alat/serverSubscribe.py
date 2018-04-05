import paho.mqtt.client as paho
import socket, sys, datetime, time, json
import httplib, urllib
from flask import Flask, request, render_template
from random import randint
import ispu

def sensorSulfur():
	sensor = randint(80,2620)
	return sensor

def sensorOzon():
	sensor = randint(120,1200)
	return sensor

def sensorNitrogen():
	sensor = randint(0,3750)
	return sensor

def timeStamp():
	ts = time.time()
	waktu = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
	return waktu

def on_subscribe(client, userdata, mid, granted_qos):
    print("STATUS : " + str(mid) + " NODE SUBSCRIBED")

def on_message(client, userdata, msg):
	respon = json.loads(str(msg.payload))
	# print "Message from SMOQ : ", respon
	asap = int(respon['asap'])
	karbon = int (respon['karbon'])
	sulfur = sensorSulfur()
	ozon = sensorOzon()
	nitrogen = sensorNitrogen()

	status = ispus(asap, sulfur, karbon, ozon, nitrogen)
	kirim(asap, sulfur, karbon, ozon, nitrogen, status, timeStamp())

def ispus(asap, sulfur, karbon, ozon, nitrogen):
	datas = [asap, sulfur, karbon, ozon, nitrogen]
	ispuval = ispu.get_ispu(datas)
	kategori = ispu.get_kategori(ispuval)
	return kategori

def kirim(asap, sulfur, karbon, ozon, nitrogen, status="", time=""):
	conn = httplib.HTTPConnection('ngehubx.online:7777')
	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	data = {'asap': asap, 'sulfur': sulfur, 'karbon' : karbon, 
		'ozon': ozon, 'nitrogen': nitrogen, 'status': status, 'time': time}
	print "Data Sent : \n", data
	params = urllib.urlencode(data)
	conn.request("POST", "/sensor/training", params, headers)
	response = conn.getresponse()
	print response.read()

client = paho.Client()
client.username_pw_set("admintes", "admin123")
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("ngehubx.online", 1883)
#topic yang di publish rafi
client.subscribe("project/dataSensor")

client.loop_forever()