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
	bloodGroup = raw_input("Enter Blood Group :")
	RhFactor =raw_input("Enter RhFactor Type:")
	gender =raw_input("Enter Gender :")
	dob = raw_input("enter date of birth :")
	workLocation =raw_input("Enter work location :")
	homeLocation = raw_input("Enter home location :")
	#postedDate =raw_input("Enter Posted date :")
	status = raw_input("Enter Status 0 or 1 :")
	ts = time.time()
	postedDateTime =datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
	try:
		cursor.execute("INSERT INTO donorsRegistration(name, blood_group, rh_factor, gender, dob, workLocation, homeLocation, postedDate, status) VALUES(%s, %s, %s, %s, %s,%s, %s, %s, %s)", (name, bloodGroup, RhFactor, gender, dob, workLocation, homeLocation, postedDateTime, status))
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
