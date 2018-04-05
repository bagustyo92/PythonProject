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
	# print str(respon['g1'])

	# LIST TO DO BIAR DINAMIS YA OPO
	sensor = 
	[respon['g1'], respon['g2'], respon['g3'], respon['g4'], respon['g5'], respon['g6'],
	respon['g7'], respon['g8'], respon['g9'], respon['g10'],
	respon['g11'], respon['g12'], respon['g13'], respon['g14'], respon['g15'], respon['g16'],
	respon['g17'], respon['g18'], respon['g19'], respon['g20'],
	respon['g21'], respon['g22'], respon['g23'], respon['g24'], respon['g25'], respon['g26'],
	respon['g27'], respon['g28'], respon['g29']]

	# LIST TO DO BIAR DINAMIS YA OPO
	for i in range (1, 28) :
		g[i] = prosesBayes(str(i), respon['g', str(i)])
	g1 = prosesBayes("1", respon['g1'])
	g2 = prosesBayes("2", respon['g2'])
	g3 = prosesBayes("3", respon['g3'])
	g4 = prosesBayes("4", respon['g4'])
	g5 = prosesBayes("5", respon['g5'])
	g6 = prosesBayes("6", respon['g5'])
	g7 = prosesBayes("7", respon['g5'])
	g8 = prosesBayes("8", respon['g5'])
	g9 = prosesBayes("9", respon['g5'])
	g10 = prosesBayes("10", respon['g10'])
	#LIST TO DO MAKE IT TILL 29
	
	# print "g1 : ", g1
	# print "g2 : ", g2
	# print "g3 : ", g3
	# print "g4 : ", g4
	# print "g5 : ", g5

	# BELOM SAMPE SINI 
	bayes=[]
	print "DATA SENSOR : ", respon['g1'], respon['g2'], respon['g3'], respon['g4'], respon['g5'], respon['timestamp']
	for n in range (5) :
		hitung = g1[n] * g2[n] * g3[n] * g4[n] * g5[n]
		print "hitung", n, ":", g1[n], g2[n], g3[n], g4[n], g5[n]
		bayes.append(hitung)
	print "DATA SENSOR : ", respon['g1'], respon['g2'], respon['g3'], respon['g4'], respon['g5'], respon['timestamp']
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
	kirim(respon['g1'], respon['g2'], respon['g3'], respon['g4'], respon['g5'], status, respon['timestamp'])
	kirimPlatform(respon['timestamp'], status, nilaiStatus, sensor)

# def kirimPlatform(time, status, nilaiStatus, dataSensor):
# 	negara = ['Indonesia', 'Singapura', 'Filipina', 'Brunei', 'Laos', 'Kamboja']
# 	pesan = {'timestamp' : time, 'classified' : status, 'tipe' : 'Bayes', 'nilai_ispu' : nilaiStatus, 'kategori_ispu' : status, 'place' : negara[randint(0,5)], 'data' : dataSensor}
# 	kirim = json.dumps(pesan)
# 	print kirim
# 	client.publish("project/pengpol", kirim)

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

# def kirim(g1, g2, g3, g4, g5, status="", time=""):
# 	conn = httplib.HTTPConnection('ngehubx.online:7777')
# 	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
# 	params = urllib.urlencode({'g1': g1, 'g2': g2, 'g3' : g3, 'g4': g4, 'g5' : g5, 'status': status, 'time' : time})
# 	conn.request("POST", "/sensor/testing", params, headers)
# 	response = conn.getresponse()
# 	print response.read()

client = paho.Client()
client.username_pw_set("admintes", "admin123")
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("ngehubx.online", 1883)
#topic yang di publish rafi
client.subscribe("project/dataSensor")

client.loop_forever()