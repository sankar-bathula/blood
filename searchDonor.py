import MySQLdb
db=MySQLdb.connect('localhost', 'root', '', 'bloom')
cursor = db.cursor()

def searchData():
	data = " SELECT * FROM donorsRegistration "
	for row in cursor.execute(data):
		print(row)
		#print(row[0])

searchData()