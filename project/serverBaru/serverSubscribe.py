import paho.mqtt.client as paho
import socket, sys, datetime, time, json
import httplib, urllib
from flask import Flask, request, render_template
from random import randint

sensor=[]

def on_subscribe(client, userdata, mid, granted_qos):
    print("STATUS : " + str(mid) + " NODE SUBSCRIBED")

def on_message(client, userdata, msg):
	# print "Data " + msg.topic + " : " + str(msg.payload)
   	respon = json.loads(str(msg.payload))
	# print str(respon['asap'])
	sensor = [respon['asap'], respon['sulfur'], respon['karbon'], respon['ozon'], respon['nitrogen']]
	asap = prosesBayes("asap", respon['asap'])
	sulfur = prosesBayes("sulfurdioksida", respon['sulfur'])
	karbon = prosesBayes("karbonmonoksida", respon['karbon'])
	ozon = prosesBayes("ozon", respon['ozon'])
	nitrogen = prosesBayes("nitrogendioksida", respon['nitrogen'])
	# print "ASAP : ", asap
	# print "SULFUR : ", sulfur
	# print "KARBON : ", karbon
	# print "OZON : ", ozon
	# print "NITROGEN : ", nitrogen
	bayes=[]
	print "DATA SENSOR : ", respon['asap'], respon['sulfur'], respon['karbon'], respon['ozon'], respon['nitrogen'], respon['timestamp']
	for n in range (5) :
		hitung = asap[n] * sulfur[n] * karbon[n] * ozon[n] * nitrogen[n]
		print "hitung", n, ":", asap[n], sulfur[n], karbon[n], ozon[n], nitrogen[n]
		bayes.append(hitung)
	print "DATA SENSOR : ", respon['asap'], respon['sulfur'], respon['karbon'], respon['ozon'], respon['nitrogen'], respon['timestamp']
	print "PERHITUNGAN BAYES : ", bayes
	print "MAX BAYES : ", max(bayes)
	i = 0
	idx = 0
	mx = 0
	for n in bayes :
		if bayes[i] == max(bayes) :
			idx = i
		i += 1
	# print max(bayes)
	print "INDEX : ", idx
	status = ""
	for n in bayes :
		if idx == 0 :
			status = "Baik"
			nilaiStatus = randint(0, 50)
		elif idx == 1 :
			status = "Sedang"
			nilaiStatus = randint(51, 100)
		elif idx == 2 :
			status = "Tidak Sehat"
			nilaiStatus = randint(101, 199)
		elif idx == 3 :
			status = "Sangat Tidak Sehat"
			nilaiStatus = randint(200, 299)
		elif idx == 4 :
			status = "Berbahaya"
			nilaiStatus = randint(300, 500	)
	print "STATUS : ", status
	print "RANDOM ISPU : ", nilaiStatus
	kirim(respon['asap'], respon['sulfur'], respon['karbon'], respon['ozon'], respon['nitrogen'], status, respon['timestamp'])
	kirimPlatform(respon['timestamp'], status, nilaiStatus, sensor)

def kirimPlatform(time, status, nilaiStatus, dataSensor):
	negara = ['Indonesia', 'Singapura', 'Filipina', 'Brunei', 'Laos', 'Kamboja']
	pesan = {'timestamp' : time, 'classified' : status, 'tipe' : 'Bayes', 'nilai_ispu' : nilaiStatus, 'kategori_ispu' : status, 'place' : negara[randint(0,5)], 'data' : dataSensor}
	kirim = json.dumps(pesan)
	print kirim
	client.publish("project/pengpol", kirim)

def prosesBayes(dataParamater, respon) :
	conn = httplib.HTTPConnection('ngehubx.online:7777')
	conn.request("GET", "/bayes/"+ dataParamater + "/" + str(	respon))
	response = conn.getresponse()
	if response.status == 200 :
		resp = json.loads(response.read())
		for n in resp["data_sensor"] :
			if n["status"] == "Baik" :
				# status.insert(0, n["status"])
				if n["bayes_calculation"][0] == None :
					n["bayes_calculation"][0] = 0
				baik = float(n["bayes_calculation"][0]) / float(n["bayes_calculation"][1])
			elif n["status"] == "Sedang" :
				if n["bayes_calculation"][0] == None :
					n["bayes_calculation"][0] = 0
				sedang = float(n["bayes_calculation"][0]) / float(n["bayes_calculation"][1])
				# status.insert(1, n["status"])
			elif n["status"] == "Tidak Sehat" :
				# status.insert(2, n["status"])
				if n["bayes_calculation"][0] == None :
					n["bayes_calculation"][0] = 0
				tdk_sehat = float(n["bayes_calculation"][0]) / float(n["bayes_calculation"][1])
			elif n["status"] == "Sangat Tidak Sehat" :
				# status.insert(3, n["status"])
				if n["bayes_calculation"][0] == None :
					n["bayes_calculation"][0] = 0
				sgt_tdk_sehat = float(n["bayes_calculation"][0]) / float(n["bayes_calculation"][1])
			elif n["status"] == "Berbahaya" :
				# status.insert(4, n["status"])
				if n["bayes_calculation"][0] == None :
					n["bayes_calculation"][0] = 0
				berbahaya = float(n["bayes_calculation"][0]) / float(n["bayes_calculation"][1])
		return [baik, sedang, tdk_sehat, sgt_tdk_sehat, berbahaya]
	elif response.status == 404 :
		return 'error'

def kirim(asap, sulfur, karbon, ozon, nitrogen, status="", time=""):
	conn = httplib.HTTPConnection('ngehubx.online:7777')
	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	params = urllib.urlencode({'asap': asap, 'sulfur': sulfur, 'karbon' : karbon, 'ozon': ozon, 'nitrogen' : nitrogen, 'status': status, 'time' : time})
	conn.request("POST", "/sensor/testing", params, headers)
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