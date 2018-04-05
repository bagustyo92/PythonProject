import socket, sys, datetime, time, json
from flask import Flask, abort
from thread import start_new_thread

PORT = 6666
MAX = 65535
pesan = []
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', PORT))
print "Server Ready\n"

def udpServer():
	try:
		while True: 
			data, address = s.recvfrom(MAX)
			print "Data Received From Node"
			obj = json.loads(data)
			print obj
			pesan.insert(0,obj)
			#pesan.insert(0, json.loads(data))
			#print pesan
			#obj = json.loads(pesan)
			#print obj
	except KeyboardInterrupt :
		print "\n CANCELED"
		sys.exit()

app = Flask(__name__)

@app.route('/node', methods=['GET'])
def semua():
	return json.dumps(pesan)

@app.route('/node/<int:node_id>', methods=['GET'])
def satu(node_id):
	node = None
	for n in pesan :
		if n["id"] == node_id :
			node = n
	if node :
		return json.dumps(node)
	else :
		abort(404)

if __name__=='__main__':
	start_new_thread(udpServer, ())
	app.run(debug=True, port=7777, use_reloader=False)