import MySQLdb

db1 = MySQLdb.connect(host="localhost", user="root", passwd="MilikBersama")
cursor = db1.cursor()
sql = 'CREATE DATABASE project'
cursor.execute(sql)