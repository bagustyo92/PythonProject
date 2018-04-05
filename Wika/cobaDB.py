import MySQLdb

db = MySQLdb.connect(host="188.166.245.69", 
					user="wgDashProdUser", 
					passwd="w1k4gedung", 
					db="wg_dashboard_production")
cursor = db.cursor()
query = "SELECT email FROM db_mobile_user WHERE email IS NOT NULL"
cursor.execute(query)
db.commit()

numrows = cursor.rowcount
emailUser = ""
for x in range(0, numrows):
    row = cursor.fetchone()
    email = row[0].strip()
    if (emailUser == ""):
    	emailUser = str(email)
    else :
    	emailUser = str(emailUser) + ", " + str(email)

print emailUser

db.close()