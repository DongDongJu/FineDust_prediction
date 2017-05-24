class Data:
	def __init__(self,site,detail_site,year,month,day,pm10,pm25="-"):
		self.site=site
		self.detail_site=detail_site
		self.year=year
		self.month=month
		self.day=day
		self.pm10=pm10
		self.pm25=pm25
	def __repr__(self):
		re=self.site+" "+self.detail_site+" "+self.year+" "+self.month+" "+self.day+" "+self.pm10+" "+self.pm25
		return re 

class DataSet:
	def __init__(self):
		self.data_list=[]

	def Add_Data(self,Data):
		self.data_list.append(Data)

	def Print_Data(self):
		for data in self.data_list:
			print(data)
