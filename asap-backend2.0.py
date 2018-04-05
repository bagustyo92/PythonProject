import serial
import time
import os
import requests
import sys
import json
import random
import string 
import requests.packages.urllib3
from twython import Twython

def request(sensorValue, dirValue, name):
	print 'Uploading ' + name + ' Data Sensor ...'
	requests.packages.urllib3.disable_warnings()
	result = requests.put(firebase_url + '/' + dirValue + '/.json' + '?auth=' + auth_token, data=json.dumps(sensorValue))
	print 'Record inserted. Result Code = ' + str(result.status_code)
	print '------------------------------------------\n'	
	if (name=='FAN'):
		print 'All Data Sensor has been uploaded, dude!\n'
		time.sleep(1)
		os.system('cls')

def acak(length):
	string_all = string.letters+string.digits
	return ''.join(random.choice(string_all) for i in range(2*length))

def masuk_jam(normalValue):
	content = " "
	strNorValue = str(normalValue)
	if (normalValue>200):
		if (normalValue>400):
			status_jam = 'Siaga'
			code_jam = 'SIA-'
		else:
			status_jam = 'Waspada'
			code_jam = 'WAS-'
	else:
		status_jam = "Normal"
		code_jam = "NOR-"

	print 'MASUK JAM'
	content = "@iPamungkasss " + "\n" + "Kadar Asap (PPM) : " + strNorValue + "\n" + "Status : " + status_jam + "\n" + "Code : " + code_jam + acak(3) + "\n\n\n" + "#ASAPMonitoring #ETIME2016"
	twitter.update_status(status=content)
	print 'tweet sent... \n'

def masuk_kondisi(initValue, status, code):
	content = " "
	strValue = str(initValue)
	print 'MASUK JAM'
	content = "@iPamungkasss " + "\n" + "Kadar Asap (PPM) : " + strValue + "\n" + "Status : " + status + "\n" + "Code : " + code + acak(3) + "\n\n\n" + "#ASAPMonitoring #Bluetechfest"
	print 'tweet sent... \n'
	
#Setup a loop to send Temperature values at fixed intervals
fixed_interval = 1
start_interval = 2

#Init Firebase
firebase_url = 'https://resplendent-heat-8054.firebaseio.com'
auth_token = 'RRgoYFKBnOXIejFKAaTHxuqjCZWB3ARZi6MeHGpa'

#Init TwitBot
CONSUMER_KEY = '7uBhEGYqgwE11PFj9UXz8fSpe'
CONSUMER_SECRET = 'oSgB3ZVlvFOiug69yPDuzXW7ZCEwDuSL07t36lbKoA6WD8k0vr'
ACCESS_KEY = '4114832412-BNhCX14DkcJnQYRZ9EQph6MumG2QvvU3i2tWVkn'
ACCESS_SECRET = '1U7l0uD6jtcMJD2fy8lRrLv5PogjHAHzrl0evquZOQIt2'
twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#INIT TIME
jamPagi = "08:45"
jamSiang = "15:53"
jamSore = "16:00"
jamMalam = "00:51"
count = 0
hitungSiaga = 0
hitungWaspada = 0
time_control=False
status_cond = " "
code_cond = " "


#Connect to Serial Port for communication
try:
	ser = serial.Serial('COM4', 9600, timeout=0)
	os.system('cls')
	print '=========================='
	print 'Welcome to ASAP-Monitoring'
	print 'Getting Started ...'
	print '==========================\n'
	time.sleep(start_interval)
		
	read_out = False

	while 1:
		read_temp = False
		read_in = False
		read_sensor = False
	
		#read Sensor
		if count==0 or read_out==False: #jangan lupa diganti True
			# temp = ser.readline()
			in2 = ser.readline()
			out2 = ser.readline()
			in7 = ser.readline()
			out7 = ser.readline()			
			fan = ser.readline()
			
			#simulation here
			temp = "27\r\n"
			
			#print value
			print '============='
			print 'Data Sensor\n'
			print 'FAN     : ' + fan + 'Suhu    : ' + temp + 'MQ2-IN  : ' + in2 +  'MQ2-OUT : ' + out2 + 'MQ7-IN  : ' + in7 + 'MQ7-OUT : ' + out7 + '=============\n'
			read_sensor = True
		else:
			print 'System cannot read the sensor'
			break
		
		#Request-ing Data Sensor
		i=1
		while (i<=6):
			if i == 1:
				# strTemp = str(int(temp))
				dataSensor = {'value':temp}
				dirSensor = 'temp'
				namaSensor = 'Temp'
			elif i == 2:
				# strIn2 = str(int(in2))
				dataSensor = {'value':in2}
				dirSensor = 'mq2-in'
				namaSensor = 'MQ2 IN'
			elif i == 3:
				# strOut2 = str(int(out2))
				dataSensor = {'value':out2}
				dirSensor = 'mq2-out'
				namaSensor = 'MQ2 OUT'
			elif i == 4:
				# strIn7 = str(int(in7))
				dataSensor = {'value':in7}
				dirSensor = 'mq7-in'
				namaSensor = 'MQ7 IN'
			elif i == 5:
				# strOut7 = str(int(out7))
				dataSensor = {'value':out7}
				dirSensor = 'mq7-out'
				namaSensor = 'MQ7 OUT'
			else:
				strFan = str(int(fan))
				dataSensor = {'value':strFan}
				dirSensor = 'fan-1'
				namaSensor = 'FAN'
			
			request(dataSensor, dirSensor, namaSensor)
			i = i + 1

		# init value
		newCond = int(in2)
		newCondValue = str(newCond)
		now = time.strftime("%H:%M")

		# init twitter conn
		if count==0:
			print 'MASUK INIT'
			content = "Device has been connected" + "\n" + "Code : " + acak(5) + "\n\n\n" + "#ASAPMonitoring #ETIME2016"
			twitter.update_status(status=content)
			print 'tweet sent... \n'
		else:
			if newCond>200:
				if newCond>400:
					if hitungSiaga == 0 or hitungSiaga == 50:
						print 'Masuk Siaga'
						status_cond = 'Siaga'
						code_cond = 'SIA-'
					hitungSiaga = hitungSiaga + 1
					print hitungSiaga
				else:
					if hitungWaspada == 0 or hitungWaspada == 100:
						print 'Masuk Waspada'
						status_cond = 'Waspada'
						code_cond = 'WAS-'
					hitungWaspada = hitungWaspada + 1
					print hitungWaspada
			masuk_kondisi(newCond, status_cond, code_cond)

		# print now
		if now==jamPagi or now==jamSiang or now==jamSore or now==jamMalam:
			if time_control==False:
				masuk_jam(newCond)
				time_control=True
			else:
				print 'gaboleh banyak nge-tweet gan, tadi kan udah yee :p'
		else:
			print 'belum waktunya nih gan'
			time_control=False				

		count = count + 1
		time.sleep(fixed_interval)
		# time.sleep(30)

except serial.SerialException:
	print '\nSerial communication cannot established, dude'
	print '----------------------------------------------'
except IOError:
	print('Error! Something went wrong.')
except KeyboardInterrupt:
	print('\n\nOPERATION HAS BEEN CANCELED!\n')
	sys.exit()
	
print 'System has been exit'
sys.exit()