import grs
from grs import TWSENo
from grs import Stock
twse_no = TWSENo()
for i in twse_no.all_stock_no:
	if len(i) <= 4 :
		stock = Stock(i, 12)
		file_locate = "/Users/Mac/Desktop/Stock Research/DataBase2/" + i + ".csv"
		stock.out_putfile(file_locate)