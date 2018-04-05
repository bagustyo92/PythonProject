# import logging
# from logging.handlers import RotatingFileHandler
import MySQLdb
from flask import Flask, abort, request
import json

app = Flask(__name__)

def gejala(value):
    if (value==1):
        return "g1"
    elif (value==2):
        return "g2"
    elif (value==3):
        return "g3"
    elif (value==4):
        return "g4"
    elif (value==5):
        return "g5"
    elif (value==6):
        return "g6"
    elif (value==7):
        return "g7"
    elif (value==8):
        return "g2"
    elif (value==9):
        return "g3"
    elif (value==10):
        return "g4"
    elif (value==11):
        return "g5"
    elif (value==12):
        return "g6"
    elif (value==13):
        return "g7"
    elif (value==14):
        return "g2"
    elif (value==15):
        return "g3"
    elif (value==16):
        return "g4"
    elif (value==17):
        return "g5"
    elif (value==18):
        return "g6"
    elif (value==19):
        return "g7"
    elif (value==10):
        return "g3"
    elif (value==21):
        return "g4"
    elif (value==22):
        return "g5"
    elif (value==23):
        return "g6"
    elif (value==24):
        return "g7"
    elif (value==25):
        return "g2"
    elif (value==26):
        return "g3"
    elif (value==27):
        return "g4"
    elif (value==28):
        return "g5"
    elif (value==29):
        return "g6"    

def kategoriSensor(value):
    if (value < 1):
        return ["Error", 0, 0]
    elif (value < 51):
        return ["Baik", 1, 50]
    elif (value < 101):
        return ["Sedang", 51, 100]
    elif (value < 200):
        return ["Tidak Sehat", 101, 200]
    elif (value < 300):
        return ["Sangat Tidak Sehat", 200, 300]
    else:
        return ["Berbahaya", 300, 1000]

def initSensor(value):
    if (value==1):
        return "asap"
    elif (value==2):
        return "sulfurdioksida"
    elif (value==3):
        return "karbonmonoksida"
    elif (value==4):
        return "ozon"
    elif (value==5):
        return "nitrogendioksida"
    else:
        return "Error"

def initStatus(value):
    if (value==0):
        return "Baik"
    elif (value==1):
        return "Sedang"
    elif (value==2):
        return "Tidak Sehat"
    elif (value==3):
        return "Sangat Tidak Sehat"
    elif (value==4):
        return "Berbahaya"
    else:
        return "Error"

def printAll(sql):
    coreData = {"data_sensor": []}
    db = MySQLdb.connect("localhost","root","MilikBersama","project")
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        print (e)
        return None

    for row in result:
        data = row[0]
        asap = row[1]
        so2 = row[2]
        co = row[3]
        ozon = row[4]
        no2 = row[5]
        status = row[6]
        timestamp = row[7]
        message = { "id": data,
                    "partikulat":
                    {
                        "value": asap,
                        "info":
                        [
                            kategoriSensor(asap)[0],kategoriSensor(asap)[1],kategoriSensor(asap)[2]
                        ]
                    },
                    "sulfurdioksida":
                    {
                        "value": so2,
                        "info":
                        [
                            kategoriSensor(so2)[0],kategoriSensor(so2)[1],kategoriSensor(so2)[2]
                        ]
                    },
                    "karbonmonoksida":
                    {
                        "value": co,
                        "info":
                        [
                            kategoriSensor(co)[0],kategoriSensor(co)[1],kategoriSensor(co)[2]
                        ]
                    },
                    "ozon":
                    {
                        "value": ozon,
                        "info":
                        [
                            kategoriSensor(ozon)[0],kategoriSensor(ozon)[1],kategoriSensor(ozon)[2]
                        ]
                    },
                    "nitrogendioksida":
                    {
                        "value": no2,
                        "info":
                        [
                            kategoriSensor(no2)[0],kategoriSensor(no2)[1],kategoriSensor(no2)[2]
                        ]
                    },
                    "status": status,
                    "timestamp": timestamp
                }
        coreData["data_sensor"].append(message)
    db.close()
    return coreData

def printMin(sql, id_sensor):
    coreData = {"data_sensor": []}
    db = MySQLdb.connect("localhost","root","MilikBersama","project")
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        print (e)
        return None

    for row in result:
        data = row[0]
        sensor = row[1]
        status = row[2]
        timestamp = row[3]
        message = { "id": data,
                    "sensor":
                    {
                        "name": initSensor(id_sensor),
                        "value": sensor,
                        "kategori": kategoriSensor(sensor)[0]
                    },
                    "status": status,
                    "timestamp": timestamp
                }
        coreData["data_sensor"].append(message)
    db.close()
    return coreData

def printBayes(sql, nameSensor):
    coreData = {"data_sensor": []}
    db = MySQLdb.connect("localhost","root","MilikBersama","project")
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        print (e)
        return None

    for row in result:
        sensor = row[0]
        overall = row[1]
        status = row[2]
        message = { "status": status,
                    "bayes_calculation":
                    [
                        sensor, overall
                    ]
                }
        coreData["data_sensor"].append(message)
    db.close()
    return coreData

#Get all data sensor
@app.route('/', methods=['GET'])
def all():
    sql = "SELECT * FROM dataSensor"
    message = printAll(sql)

    if message["data_sensor"] :
        return json.dumps(message)
    else :
        abort(404)

#Get all data from spesific sensor
@app.route('/sensor/<int:id_sensor>', methods=['GET'])
def sensor(id_sensor):
    sql = "SELECT id, %s, status, timestamp FROM dataSensor" % (initSensor(id_sensor))
    message = printMin(sql, id_sensor)

    if message["data_sensor"] :
        return json.dumps(message)
    else :
        abort(404)

#Get all data from spesific overall status
@app.route('/sensor/overall/<int:id_status>', methods=['GET'])
def status(id_status):
    sql = "SELECT * FROM dataSensor WHERE status = '%s'" % (initStatus(id_status))
    message = printAll(sql)

    if message["data_sensor"] :
        return json.dumps(message)
    else :
        abort(404)

#Get all data from spesific date
@app.route('/sensor/date/<string:date>', methods=['GET'])
def date(date):
    date = date + "%"
    sql = "SELECT * FROM dataSensor WHERE timestamp LIKE '%s'" % (date)
    message = printAll(sql)

    if message["data_sensor"] :
        return json.dumps(message)
    else :
        abort(404)

#Get all data from spesific sensor and spesific status
@app.route('/<int:id_sensor>/<int:id_status>', methods=['GET'])
def sensor_status(id_sensor, id_status):
    sql = "SELECT id, %s, status, timestamp FROM dataSensor WHERE status = '%s'" % (initSensor(id_sensor), initStatus(id_status))
    message = printMin(sql, id_sensor)

    if message["data_sensor"] :
        return json.dumps(message)
    else :
        abort(404)

#Get all data from spesific sensor and spesific date
@app.route('/sensor/<int:id_sensor>/<string:date>', methods=['GET'])
def sensor_date(id_sensor, date):
    date = date + "%"
    sql = "SELECT id, %s, status, timestamp FROM dataSensor WHERE timestamp LIKE '%s'" % (initSensor(id_sensor), date)
    message = printMin(sql, id_sensor)

    if message["data_sensor"] :
        return json.dumps(message)
    else :
        abort(404)

#Get all data from spesific status and spesific date
@app.route('/status/<int:id_status>/<string:date>', methods=['GET'])
def status_date(id_status, date):
    date = date + "%"
    sql = "SELECT * FROM dataSensor WHERE status = '%s' AND timestamp LIKE '%s'" % (initStatus(id_status), date)
    message = printAll(sql)

    if message["data_sensor"] :
        return json.dumps(message)
    else :
        abort(404)

#Get all data from spesific sensor, spesific status and spesific date
@app.route('/<int:id_sensor>/<int:id_status>/<string:date>', methods=['GET'])
def allin(id_sensor, id_status, date):
    date = date + "%"
    sql = "SELECT id, %s, status, timestamp FROM dataSensor WHERE status = '%s' AND timestamp LIKE '%s'" % (initSensor(id_sensor), initStatus(id_status), date)
    message = printMin(sql, id_sensor)

    if message["data_sensor"] :
        return json.dumps(message)
    else :
        abort(404)

#naive bayes api support
@app.route('/bayes/<int:nameSensor>/<int:sensorValue>', methods=['GET'])
def bayes(nameSensor, sensorValue):
    sql = "SELECT A.sensor, B.overall, B.penyakit FROM (SELECT COUNT(penyakit) AS sensor, penyakit FROM dataPenyakit WHERE %s = %i GROUP BY penyakit) A RIGHT JOIN (SELECT COUNT(penyakit) AS overall, penyakit FROM dataPenyakit GROUP BY penyakit) B ON A.penyakit = B.penyakit" % (gejala(nameSensor), sensorValue)
    # print sql
    message = printBayes(sql, nameSensor)

    if message["data_sensor"] :
        return json.dumps(message)
    else :
        abort(404)

# #naive bayes api support penyakit
# @app.route('/penyakit/<string:nameSensor>/<int:sensorValue>', methods=['GET'])
# def bayes(nameSensor, sensorValue):
#     sql = "SELECT A.sensor, B.overall, B.penyakit FROM (SELECT COUNT(penyakit) AS sensor, penyakit FROM dataPenyakit WHERE %s = %i GROUP BY penyakit) A RIGHT JOIN (SELECT COUNT(penyakit) AS overall, penyakit FROM dataPenyakit GROUP BY penyakit) B ON A.penyakit = B.penyakit" % (gejala(nameSensor), sensorValue)
#     # print sql
#     message = printBayes(sql, nameSensor)
#
#     if message["data_sensor"] :
#         return json.dumps(message)
#     else :
#         abort(404)

#Get all data testing
@app.route('/sensor/testing/all', methods=['GET'])
def allTesting():
    sql = "SELECT * FROM dataTesting"
    message = printAll(sql)

    if message["data_sensor"] :
        return json.dumps(message)
    else :
        abort(404)

# REST WS untuk post data training
@app.route('/sensor/training', methods=['POST'])
def dataTraining():
    # Dapatkan semua data dari parameter POST yang dikirim client
    asap = request.form.get('asap')
    sulfur = request.form.get('sulfur')
    karbon = request.form.get('karbon')
    ozon = request.form.get('ozon')
    nitrogen = request.form.get('nitrogen')
    status = request.form.get('status')
    time = request.form.get('time')
    message = {}

    sql = "INSERT INTO dataSensor(asap, sulfurdioksida, karbonmonoksida, ozon, nitrogendioksida, status, timestamp) VALUES(%i, %i, %i, %i, %i, '%s', '%s')" % (int(asap), int(sulfur), int(karbon), int(ozon), int(nitrogen), status, time)
    db = MySQLdb.connect("localhost","root","MilikBersama","project")
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        message = {"status": "OK"}
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        message = {"status": "ERROR"}
        db.rollback()
        print (e)

    db.close()
    return json.dumps(message)

# REST WS untuk post data testing
@app.route('/sensor/testing', methods=['POST'])
def dataTesting():
    # Dapatkan semua data dari parameter POST yang dikirim client
    asap = request.form.get('asap')
    sulfur = request.form.get('sulfur')
    karbon = request.form.get('karbon')
    ozon = request.form.get('ozon')
    nitrogen = request.form.get('nitrogen')
    status = request.form.get('status')
    time = request.form.get('time')
    message = {}

    sql = "INSERT INTO dataTesting(asap, sulfurdioksida, karbonmonoksida, ozon, nitrogendioksida, status, timestamp) VALUES(%i, %i, %i, %i, %i, '%s', '%s')" % (int(asap), int(sulfur), int(karbon), int(ozon), int(nitrogen), status, time)
    db = MySQLdb.connect("localhost","root","MilikBersama","project")
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        message = {"status": "OK"}
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        message = {"status": "ERROR"}
        db.rollback()
        print (e)

    db.close()
    return json.dumps(message)

if __name__=='__main__':
	app.run(debug=True, host="ngehubx.online", port=7777)

