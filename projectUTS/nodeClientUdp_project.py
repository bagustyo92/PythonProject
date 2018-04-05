import socket, sys, datetime, time, json
from random import randint

SERVER_IP = '127.0.0.1'
PORT = 6666
MAX = 65535
counter = 0
def sensor():
	sensor = randint(0,100)
	return str(sensor)

while True :
	#generate timestamp
	ts = time.time()
	waktu = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
	#generate random data sensor as message between 0 to 400
	counter=counter + 1
	kirim = {'id': counter, 'temp': sensor(), 'hum': sensor(), 'smoke': sensor(), 'carbon': sensor(), 'timestamp': waktu}
	pesan = json.dumps(kirim)
	print pesan
	time.sleep(3)
	print "Sent at : ", waktu
	print "Data : ", kirim
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.sendto(pesan, (SERVER_IP, PORT))
s.close()