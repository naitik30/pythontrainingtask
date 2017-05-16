import MySQLdb
import csv
# connect
db = MySQLdb.connect(host="localhost", user="root", passwd="root",db="test")

cursor = db.cursor()

with open('FL_insurance_sample (1).csv', 'rb') as csv_file:
	csv_data = csv.reader(csv_file)
	csv_header = next(csv_data)
	sql = """CREATE TABLE FL_Insurance (
         policyID INT(20) NOT NULL,
         county CHAR(30),  
         eq_site_limit INT(20),
         hu_site_limit INT(20),
         fl_site_limit INT(20),
         fr_site_limit INT(20),
         tiv_2011 INT(20),
         tiv_2012 INT(20),
         eq_site_deductible INT(20),
		 hu_site_deductible INT(20),
		 fl_site_deductible INT(20),
		 fr_site_deductible,  INT(20),
		 point_latitude FLOAT,
		 point_longitude FLOAT,
		 line CHAR(20),
		 construction CHAR(20),
		 point_granularity INT(20)
		)"""
	cursor.execute(sql)

	for data in csv_data:
		sql = "INSERT INTO FL_Insurance(policyID,\
			county, eq_site_limit, hu_site_limit, fl_site_limit, fr_site_limit, tiv_2011, tiv_2012, \
			eq_site_deductible, hu_site_deductible, fl_site_deductible, fr_site_deductible,\
			point_latitude, point_longitude, line, construction, point_granularity) \
			VALUES ('%d', '%s', '%d','%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%f','%f',\
				'%s', '%s','%d' )" % \
			(int(data[0]), data[2], int(float(data[3])), int(float(data[4])), int(float(data[5])),\
			 int(float(data[6])), int(float(data[7])), int(float(data[8])), int(float(data[9])),\
			 int(float(data[10])), int(float(data[11])), int(float(data[12])),\
			 float(data[13]),float(data[14]),data[15],data[16],int(float(data[17])))
		try:
		# Execute the SQL command
			cursor.execute(sql)
			# Commit your changes in the database
			db.commit()
			
		except:
		# Rollback in case there is any error
			db.rollback()

cursor.close()





