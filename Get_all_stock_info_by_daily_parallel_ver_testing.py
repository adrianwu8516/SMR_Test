#Environment Setting
import grs
import sys
from grs import TWSENo
from grs import Stock
from grs import OTCNo
obj_list = []
remove_obj_list = []
twse_no = TWSENo()
otc_no = OTCNo()
month = 240

if len(sys.argv) != 3:
	print "usage: python fuckGRS.py [from_id] [to_id(not_include)]"
	sys.exit(1)

initial_idx = int(sys.argv[1])
final_idx = int(sys.argv[2])

#Build Stock List & obj_list

for i in twse_no.all_stock_no:
	if len(i) <= 4 :
		obj_list.append(i)

for i in otc_no.all_stock_no:
	if len(i) <= 4:
		obj_list.append(i)

for i in ['006203', '006204', '006205', '006206', '006207', '006208', '008201']:
	obj_list.append(i)

obj_list = obj_list[initial_idx : final_idx]
print obj_list
'''
#Helping Function
def diff(a, b):
	b = set(b)
	return [aa for aa in a if aa not in b]

#Getting Data Function
def DBuild():
	global remove_obj_list, obj_list, month
	if len(obj_list) > 0:
		for i in obj_list:			
			try:
				stock = Stock(i, month)
				file_locate = "/Users/Mac/Desktop/Stock Research/DataBase_test/" + i + ".csv"
				stock.out_putfile(file_locate)
			except AttributeError:
				print "Error >>", i, "can not fetch month = ", month
			else:
				print "Get stock no.", i, "info for", month, "month"
				remove_obj_list.append(i)
	print "Month = ", month, " : Fetching finished!"
	month = month - 1	

while month > 0:
	print "Fetching Start"
	DBuild()
	obj_list = diff(obj_list, remove_obj_list)
else:
	print "////////////////////FINISHED////////////////////"
'''