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
	raw_data.pop(0)
	return raw_data
def Check_Data(row):
	errorCode = row[2][0]
	year=row[2][:4]
	month=row[2][4:6]
	day=row[2][6:8]
	pm10=row[7]
	pm25=row[8]
	if errorCode == "1": # 2014
		year=row[3][:4]
		month=row[3][4:6]
		day=row[3][6:8]
		pm10=row[8]
		pm25="-"
	return year,month,day,pm10,pm25

class South_Korea_DataSet:
	rawdata_list=["data/South_korea/2014/2014_01.csv","data/South_korea/2014/2014_02.csv","data/South_korea/2014/2014_03.csv","data/South_korea/2014/2014_04.csv",
				  "data/South_korea/2015/2015_01.csv","data/South_korea/2015/2015_02.csv","data/South_korea/2015/2015_03.csv","data/South_korea/2015/2015_04.csv",
				  "data/South_korea/2016/2016_01.csv","data/South_korea/2016/2016_02.csv","data/South_korea/2016/2016_03.csv"] # missed 2016_04
	def __init__(self):
		self.data_set=DS.DataSet()
		for rawdata in South_Korea_DataSet.rawdata_list:
			raw_data=Csv_Reader(rawdata)
			for row in raw_data: # each row in data files ex) 서울,중구,2015010101,0.006,0.6,0.022,0.011,44,7,서울 중구 덕수궁길 15
				year,month,day,pm10,pm25=Check_Data(row)
				if year == "2014": # 2014
					data=DS.Data(row[0],row[1],year,month,day,pm10) # site,detail_site,year,month,day,pm
				else:
					data=DS.Data(row[0],row[1],year,month,day,pm10,pm25)
				self.data_set.Add_Data(data)
				if year == "2015" or year=="2014":
					print(data)
			print(rawdata+" file init compelete!")

if __name__ == "__main__":
	skd=South_Korea_DataSet()

