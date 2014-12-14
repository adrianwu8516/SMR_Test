#Environment Setting
import grs
from grs import TWSENo
from grs import Stock
obj_list = []
remove_obj_list = []
dead = 0
twse_no = TWSENo()
unable = []


#Build Stock List
for i in twse_no.all_stock_no:
	if len(i) <= 4 :
		obj_list.append(i)

#Helping Function
def diff(a, b):
        b = set(b)
        return [aa for aa in a if aa not in b]

#Getting Data
def DBuild():
	global remove_obj_list, obj_list, dead
	obj_list = diff(obj_list, remove_obj_list)
	remove_obj_list = []
	if len(obj_list) > 0:
		for i in obj_list:
			dead = i
			remove_obj_list.append(i)
			stock = Stock(i, 24)
			file_locate = "/Users/Mac/Desktop/Stock Research/DataBase_test/" + i + ".csv"
			stock.out_putfile(file_locate)
			dead = 0
	print "Yeah! Fuck you finished!"

DBuild()

#when the program was blocked run the underline function
'''
unable.append(dead)
print unable
obj_list = diff(obj_list, remove_obj_list)
remove_obj_list = []
DBuild()
'''