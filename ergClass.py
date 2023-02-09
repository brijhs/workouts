class erg: 
	__slots__ = ['_name', '_splits', '_date']
	def __init__(self, name, splits, date):
		self._name = name
		self._splits = splits
		self._date = date
	
	def getName(self):
		return self._name
	def getSplits(self):
		return self._splits
	def getDate(self):
		return self._date
	
	def __str__(self):
		return '{} at {} on {}'.format(self._name, self._splits, self._date)
def newErg():
	name = input('What was the erg workout? ')
	splits = input('What was your avg split? ')
	date = input('When was this erg workout? ')
	result = erg(name, splits, date)
	print(result)
	return result 

