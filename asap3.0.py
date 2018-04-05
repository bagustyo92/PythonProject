import serial
import time
import os
import requests
import sys
import json
import random
import string 
import requests.packages.urllib3

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
			
#Setup a loop to send Temperature values at fixed intervals
fixed_interval = 1
start_interval = 2

#Init Firebase
# firebase = firebase.FirebaseApplication('https://ramean.firebaseio.com/', None)
firebase_url = 'https://test-be923.firebaseio.com/'
auth_token = 'c2d8015d350440fca438f41a4784030f'

def main():
	#Connect to Serial Port for communication
	count = 0
	isDone = 0
	try:
		ser = serial.Serial('COM5', 9600, timeout=0)
		os.system('cls')
		print '=========================='
		print 'Welcome to ASAP-Monitoring'
		print 'Getting Started ...'
		print '==========================\n'
		time.sleep(start_interval)
		
		read_out = False

		while 1:
			isDone = 0
			print count
			print isDone
			#read Sensor
			if read_out==False: #jangan lupa diganti True
				# temp = ser.readline()
				dht = ser.readline()
				mq2 = ser.readline()
				#out2 = ser.readline()
				mq7 = ser.readline()
				mq135 = ser.readline()
				#out7 = ser.readline()			
				#fan = ser.readline()
				
				#simulation here
				#temp = "27"
				# in2 = "300\r\n"
				# out2 = "55\r\n"
				# in7 = "20\r\n"
				# out7 = "80\r\n"
				# fan = "1\r\n"
				
				#print value
				print '============='
				print 'Data Sensor\n'
				print 'Suhu    : ' + dht + 'mq2  : ' + mq2 +  'MQ 7 : ' + mq7 + 'mq135  : ' + mq135 + '=============\n'
				read_sensor = True
			else:
				print 'System cannot read the sensor'
				break

			#Request-ing Data Sensor
			i=1
			while (i<=4):
				if i == 1:
					strTemp = str(int(dht))
					dataSensor = {'value':strTemp}
					dirSensor = 'deviceTemp'
					namaSensor = 'dht'
				elif i == 2:
					#strSmokeIn = str(int(mq2))
					dataSensor = {'value':strSmokeIn}
					dirSensor = 'deviceSmokeIn'
					namaSensor = 'mq2'
				elif i == 3: 
					#strSmokeOut = str(int(mq7))
					dataSensor = {'value':strSmokeOut}
					dirSensor = 'deviceSmokeOut'
					namaSensor = 'mq7'
				else:
					#strCOIn = str(int(mq135))
					dataSensor = {'value':strCOIn}
					dirSensor = 'deviceCOIn'
					namaSensor = 'mq135'
					isDone = 1
				
				request(dataSensor, dirSensor, namaSensor)
				i = i + 1
			
			if (isDone==1):
				print 'Uploaded, dude! Sounds Great'
			else:
				print 'Oh no, Something went wrong'
			ser.write(str(isDone))
								
			count = count + 1					 
			time.sleep(fixed_interval)

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

if __name__ == '__main__':main()