import httplib, urllib
import json

def semua():
	conn = httplib.HTTPConnection('127.0.0.1:7777')
	conn.request("GET", "/node")
	response = conn.getresponse()
	resp = json.loads(response.read())
	for id in resp :
		print id["id"], id["temp"], id["humdity"]
	print resp

def satu(node_id):
	conn = httplib.HTTPConnection('127.0.0.1:7777')
	conn.request("GET", "/node/"+str(node_id))
	response = conn.getresponse()
	if response.status == 200 :
		resp = json.loads(response.read())
		
		print resp
	elif response.status == 404 :
		print "Node tidak ditemukan"
	else :
		print "Error"

semua()
satu(1)
satu(2)
satu(3)