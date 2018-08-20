from mysql.connector import MySQLConnection, Error
import MySQLdb
import time
import datetime
db =MySQLdb.connect("localhost", "root", "", "bloom")
cursor = db.cursor()
# sql = """ INSERT INTO donorsRegistration
# 	(id, name, gender, dob, workLocation, homeLocation, postedDate, status)
# 	VALUES(
# 	2, 
# 	'Bathula',
# 	'male',
# 	'12-02-1991',
# 	'Bangalore',
# 	'Hyder Nagar',
# 	'18-08-2018',
# 	'0'
# 	)"""
# try:
# 	cursor.execute(sql)
# 	db.commit()
# except:
# 	db.rollback()

def enter_dynamic_data():
	name = raw_input("Enter full name :")
	gender =raw_input("Enter Gender :")
	dob = raw_input("enter date of birth :")
	workLocation =raw_input("Enter work location :")
	homeLocation = raw_input("Enter home location :")
	#postedDate =raw_input("Enter Posted date :")
	status = raw_input("Enter Status 0 or 1 :")
	timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	try:
		print workLocation
		cursor.execute("INSERT INTO donorsRegistration(name, gender, dob, workLocation, homeLocation, postedDate, status) VALUES(%s, %s, %s,%s, %s, %s, %s)", (name, gender, dob, workLocation, homeLocation, timestamp, status))
		db.commit()
		print("Data inserted Successfully")
	except Error as error:
		db.rollback()
		print(error)


def searchData():
	data = " SELECT * FROM donorsRegistration "
	cursor.execute(data)
	for row in cursor.fetchall():
		print row

	
	# for row in cursor.execute(data):
	# 	print(row)
	# 	#print(row[0])
#searchData()
enter_dynamic_data()
db.close()
