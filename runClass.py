class run:
	__slots__ = ["_name", "_runType", "_dist", "_pace", "_date"]
	#Need these to be prompted  in newRun()
	def __init__(self, name, runType, dist, pace, date):
		self._name = name
		self._runType = runType
		self._dist = float(dist)
		self._pace = str(pace)
		self._date = str(date)

	def findName(self):
		return self._name

	def findType(self):
		return self._runType

	def findDist(self):
		return self._dist

	def findPace(self):
		return self._pace

	def findDate(self):
		return self._date
	
	
	def __str__(self):
		return str("Name: {}, Type: {}, Distance: {}, Pace: {}, Date: {}".format(self._name, self._runType, self._dist, self._pace, self._date))

def floatPace(num):
	return float(int(num[0]) + float(float(num[2:])/60))

def newRun():
	name = input("What is the name of your run? ")
	runType = input("What was the type of run? ")
	if 'back' in runType:
		runType = "Out and Back"
	elif 'oop' in runType:
		runType = "Loop"
	else:
		runType  = 'Trail'
	distance = input("How far was this run? ")
	pace = input("What was your pace? ")
	date = input("When was this run? ")
	result = run(name, runType, distance, pace, date)
	print(result)
	return result
