import MySQLdb
db = MySQLdb.connect("localhost", "bagus", "sql", "project")
cursor = db.cursor()
#cursorcute("INSERT INTO dataSensor VALUES (null, 100, 200, 300, null)")
cursor.execute("INSERT INTO dataSensor VALUES (null, 300, 200, 100, null)")
cursor.execute("SELECT * FROM dataSensor")
result = cursor.fetchall()
print (result)
db.commit()
