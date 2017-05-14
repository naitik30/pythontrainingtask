import csv

with open('FL_insurance_sample (1).csv', 'rb') as csv_file:
	data = csv.reader(csv_file)
	with open('task1.csv', 'wb') as write_file:
		data_write = csv.writer(write_file)

		for i in data:
			temp = i [:12:2]
			data_write.writerow(temp)
	write_file.close()
csv_file.close()