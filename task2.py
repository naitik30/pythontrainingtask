
print "******************************************"
print "Please enter the text which you want to  \n capitalized or enter close to terminate."
print "******************************************"


while 1:
	data = raw_input()
	
	if data == 'close':
		break
	print data.upper()

