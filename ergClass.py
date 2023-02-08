class erg: 
	__slots__ = ['_name', '_splits']
	def __init__(self, name, splits):
		self._name = name
		self._splits = splits
	
	def getName(self):
		return self._name
	def getSplits(self):
		return self._splits
	
	def __str__(self):
		return '{} at {}'.format(self._name, self._splits)
def newErg():
	name = input('What was the erg workout? ')
	splits = input('What was your avg split? ')
	result = erg(name, splits)
	print(result)
	return result 

