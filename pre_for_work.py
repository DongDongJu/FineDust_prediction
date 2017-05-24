import sys
sys.path.insert(0,"./data_model")		# for dataSet class
import csv
import os
import DataSet as DS

def Csv_Reader(file_path):
	raw_data=[]
	with open(file_path,'r') as datafile:
		reader=csv.reader(datafile,delimiter=',')
		for row in reader:
			raw_data.append(row)
	return raw_data

class South_Korea_DataSet:
	rawdata_list=["data/South_korea/2014/2014_01.csv","data/South_korea/2014/2014_02.csv","data/South_korea/2014/2014_03.csv","data/South_korea/2014/2014_04.csv",
				  "data/South_korea/2015/2015_01.csv","data/South_korea/2015/2015_02.csv","data/South_korea/2015/2015_03.csv","data/South_korea/2015/2015_04.csv",
				  "data/South_korea/2016/2016_01.csv","data/South_korea/2016/2016_03.csv","data/South_korea/2016/2016_04.csv"] # missed 2016_02
	def __init__(self):
		for rawdata in South_Korea_DataSet.rawdata_list:
			raw_data=Csv_Reader(rawdata)
			print(rawdata+" file init compelete!")

if __name__ == "__main__":
	skd=South_Korea_DataSet()

