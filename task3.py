def checklength(data1,data2):
	if len(data1) < len(data2):
		print data2
	elif len(data1) > len(data2):
		print data1
	else:
		print data1
		print data2

print "*******************************************\n"
print "both same lenth"
print "*******************************************\n"
checklength("First_and_Second_both_same","Second_and_First_both_same")


print "*******************************************\n"
print "First bigger than second"
print "*******************************************\n"

checklength("first_bigger_then_Second","second_small_then_first")


print "*******************************************\n"
print "Second bigger than first"
print "*******************************************\n"


checklength("first_small_then_Second","second_bigger_then_first")
