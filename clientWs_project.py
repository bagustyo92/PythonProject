import json, sys, simplejson
import httplib, urllib
from flask import Flask, request, render_template

app = Flask(__name__)

def semua():
	conn = httplib.HTTPConnection('127.0.0.1:7777')
	conn.request("GET", "/node")
	response = conn.getresponse()
	resp = json.loads(response.read())
	print "=================================================================="
	print ">>>>>>>>>>       HERE IS YOUR ALL DATA SENSORS         <<<<<<<<<<"
	print "=================================================================="
	for id in resp :
		print "\nID : ", id["id"], "Temperatur : ", id["temp"], "Humidity : ", id["hum"], "Smoke : ", id["smoke"], "Carbon : ", id["carbon"], "\nAt Time : ", id["timestamp"]
	print "=================================================================="
	pilih = raw_input ("\nBack To Main Menu? [Y/N] : ")
	if (pilih == "Y" or pilih == "y") :
		main()
	elif (pilih == "N" or pilih == "n") :
		print "\n>>>> THANK YOU :) <<<<"
		sys.exit()

def satu():
	masukan = raw_input ("Input Your ID Node : ")
	conn = httplib.HTTPConnection('127.0.0.1:7777')
	conn.request("GET", "/node/" + str(masukan))
	response = conn.getresponse()
	if response.status == 200 :
		resp = simplejson.loads(response.read())
		print "=================================================================="
		print ">>>>>>>>>>       HERE IS YOUR NODE DATA SENSORS         <<<<<<<<<<"
		print "=================================================================="
		print "ID : ", resp["id"], "Temperatur : ", resp["temp"], "Humidity : ", resp["hum"], "Smoke : ", resp["smoke"], "Carbon : ", resp["carbon"]
		print " At Time : ", resp["timestamp"]
		#["hum"]["smoke"]["carbon"]["timestamp"]
		# for id in resp :
		# 	print "\nID : ", str(id["id"]), "Temperatur : ", str(id["temp"]), "Humidity : ", str(id["hum"]), "Smoke : ", str(id["smoke"]), "Carbon : ", str(id["carbon"]), "\nAt Time : ", str(id["timestamp"])
		print "=================================================================="
		pilih = raw_input ("\nBack To Main Menu? [Y/N] : ")
		if (pilih == "Y" or pilih == "y") :
			main()
		elif (pilih == "N" or pilih == "n") :
			print "\n>>>> THANK YOU :) <<<<"
			sys.exit()
	elif response.status == 404 :
		print "Node tidak ditemukan"
	else :
		print "Error"

def main():
	while True :
		print "+++++++++++++++++++++++++"
		print ">>>>>>    MENU    <<<<<<"
		print "+++++++++++++++++++++++++"
		print "1. Tampilkan Semua Node"
		print "2. Tampilkan Satu Node"
		print "+++++++++++++++++++++++++"
		pilih = input ("\nInsert Your Choose : ")
		if pilih == 1 :
			semua()
		if pilih == 2 :
			satu()
main()