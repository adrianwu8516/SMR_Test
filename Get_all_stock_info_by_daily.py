#Environment Setting
import grs
from grs import TWSENo
from grs import Stock
obj_list = []
remove_obj_list = []
twse_no = TWSENo()
otc_no = OTCNo()
month = 168

#Build Stock List & obj_list
for i in twse_no.all_stock_no:
	if len(i) <= 4 :
		obj_list.append(i)

for i in otc_no.all_stock_no:
	if len(i) <= 4:
		obj_list.append(i)

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
	month = month - 12	#

while month > 0:
	print "Fetching Start"
	DBuild()
	obj_list = diff(obj_list, remove_obj_list)
else:
	print "////////////////////FINISHED////////////////////"
