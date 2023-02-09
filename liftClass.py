class lift:
	__slots__ = ['_name', '_weight', '_reps', '_date']
	def __init__(self, name, weight, reps, date):
		self._name = name
		self._weight = float(weight)
		self._reps = int(reps) 
		self._date = date

	def getName(self):
		return self._name
	def getWeight(self):
		return self._weight
	def getReps(self):
		return self._reps
	def getDate(self):
		return self._date

	def __str__(self):
		return '{} at {} lbs for {} reps on {}'.format(self._name, self._weight, self._reps, self._date)

def newLift():
	name = input("What lift did you do? ")
	weight = input("What was the weight in pounds? ")
	reps = input("How many reps did you do? ")
	date = input("When was this lift? ")
	result = lift(name, weight, reps, date)
	print(result)
	return result	
