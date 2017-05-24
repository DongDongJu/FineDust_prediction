class Day:
	def __init__(self,site,day,hour,pm):
		self.site=site
		self.day=day
		self.hour=hour
		self.pm=pm

class Month:
	def __init__(self,month,day_list):
		self.month=month
		self.day_list=day_list

class Year:
	def __init__(self,year,month_list):
		self.year=year
		self.month_list=month_list

class DataSet:
	def __init__(self,site,year_list):
		self.year_list=year_list
		self.site=site
