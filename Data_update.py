#Environment Setting
import grs
import csv
import os
from grs import TWSENo
from grs import Stock
from grs import OTCNo
from datetime import datetime
twse_no = TWSENo()
otc_no = OTCNo()
obj_list = []
handling_num = 0

#Build Stock List & obj_list

for i in twse_no.all_stock_no:
	if len(i) <= 4 :
		obj_list.append(i)

for i in otc_no.all_stock_no:
	if len(i) <= 4:
		obj_list.append(i)

for i in ['006203', '006204', '006205', '006206', '006207', '006208', '008201']:
	obj_list.append(i)

for stock_num in obj_list:
	try:	
		handling_num = stock_num
		temp_list_old = []
		temp_list_index = []
		indicator = True
		obj_filename = stock_num + ".csv"

		csvfile = open(obj_filename, 'rb') 
		for i in csv.reader(csvfile, delimiter=','): 
			temp_list_index.append(i[0])
			temp_list_old.append(i)

		stock = Stock(stock_num, 4)    
		stock.out_putfile("temp.csv")    
		
		csvfile = open("temp.csv", 'rb') 
		for i in csv.reader(csvfile, delimiter=','):
			indicator = True
			for index in temp_list_index:
				if str(i[0]) == index:
					indicator = False
					break
			if indicator:
				temp_list_old.append(i)

		with open(obj_filename, 'wt') as i:
			output = csv.writer(i)
			for row in temp_list_old:
				output.writerow(row)
	except IOError:
		print "ERROR >> " +  stock_num
		stock = Stock(stock_num, 3) 
		file_locate = stock_num + ".csv"
		stock.out_putfile(file_locate)

print "Finished!"
