class lift:
	__slots__ = ['_name', '_weight', '_reps']
	def __init__(self, name, weight, reps):
		self._name = name
		self._weight = float(weight)
		self._reps = int(reps) 

	def getName(self):
		return self._name
	def getWeight(self):
		return self._weight
	def getReps(self):
		return self._reps

	def __str__(self):
		return '{} at {} lbs for {} reps'.format(self._name, self._weight, self._reps)

def newLift():
	name = input("What lift did you do? ")
	weight = input("What was the weight in pounds? ")
	reps = input("How many reps did you do? ")
	result = lift(name, weight, reps)
	print(result)
	return result	
