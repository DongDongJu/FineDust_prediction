import sys
sys.path.insert(0,"./data_model")		# for dataSet class
import os
import data_model.DataSet as DS
import csv

def Csv_Reader(file_path):
	raw_data=[]
	with open(file_path,"r",encoding="utf-8") as datafile:
		reader=csv.reader(datafile,delimiter=',')
		for row in reader:
			raw_data.append(row)
	raw_data.pop(0)
	return raw_data

def Check_Data_Korea(row):
	if len(row[2]) == 6: # 2014
		year=row[3][:4]
		month=row[3][4:6]
		day=row[3][6:8]
		pm10=row[8]
		pm25="-"
	else:
		year = row[2][:4]
		month = row[2][4:6]
		day = row[2][6:8]
		pm10 = row[7]
		try:
			pm25 = int(row[8])
			South_Korea_DataSet.lastest_pm25 = pm25
		except:
			pm25 = South_Korea_DataSet.lastest_pm25
	return year,month,day,pm10,pm25

def checkNull(rawData):
	for raw in rawData:
		if raw[8] == '':
			year = raw[2][:4]
			month = raw[2][4:6]
			day = raw[2][6:8]
			pm10 = raw[7]
			pm25 = raw[8]
			sum = 0
			cnt = 0
			city = raw[0]
			borough = raw[1]
			for data in rawData:
				if (city == data[0] and borough == data[1] and year == data[2][:4] and month == data[2][4:6] and day == data[2][6:8]):
					if data[8] != '':
						sum += int(data[8])
						cnt += 1
			raw[8] = str(sum / cnt)

def Check_Data_China(row):
	year=row[3]
	month=row[4]
	day=row[5]
	pm10="-"
	try:
		pm25=int(row[7])
		China_DataSet.lastest_pm25=pm25
	except:
		pm25=China_DataSet.lastest_pm25
	return year,month,day,pm10,pm25

class South_Korea_DataSet:
	rawdata_list=["data/South_korea/2014/2014_01.csv","data/South_korea/2014/2014_02.csv","data/South_korea/2014/2014_03.csv","data/South_korea/2014/2014_04.csv",
				  "data/South_korea/2015/2015_01.csv","data/South_korea/2015/2015_02.csv","data/South_korea/2015/2015_03.csv","data/South_korea/2015/2015_04.csv",
				  "data/South_korea/2016/2016_01.csv","data/South_korea/2016/2016_02.csv","data/South_korea/2016/2016_03.csv"] # missed 2016_04
	lastest_pm25=-1
	def __init__(self):
		self.data_set=DS.DataSet()
		for rawdata in South_Korea_DataSet.rawdata_list:
			raw_data=Csv_Reader(rawdata)
			for row in raw_data: # each row in data files ex) 서울,중구,2015010101,0.006,0.6,0.022,0.011,44,7,서울 중구 덕수궁길 15
				year,month,day,pm10,pm25=Check_Data_Korea(row)
				if year == "2014": # 2014
					data=DS.Data(row[0],row[1],year,month,day,pm10) # site,detail_site,year,month,day,pm
				else:
					data=DS.Data(row[0],row[1],year,month,day,pm10,pm25)
				self.data_set.Add_Data(data)
			print(rawdata+" file init compelete!")

class China_DataSet:
	rawdata_list=["data/China/Beijing/2014.csv","data/China/Beijing/2015.csv","data/China/Beijing/2016.csv","data/China/Beijing/2017.csv","data/China/Shanghai/2014.csv","data/China/Shanghai/2015.csv","data/China/Shanghai/2016.csv","data/China/Shanghai/2017.csv","data/China/Shenyang/2014.csv","data/China/Shenyang/2015.csv","data/China/Shenyang/2016.csv","data/China/Shenyang/2017.csv"]
	lastest_pm25=-1
	def __init__(self):
		self.data_set=DS.DataSet()
		for rawdata in China_DataSet.rawdata_list:
			raw_data=Csv_Reader(rawdata)
			for row in raw_data:
				year,month,day,pm10,pm25=Check_Data_China(row)
				data=DS.Data("China",row[0],year,month,day,pm10,pm25)
				self.data_set.Add_Data(data)
			print(rawdata+" file init compelete!")