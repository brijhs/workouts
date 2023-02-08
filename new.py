from writeRun import *
from writeerg import *
from writelift import *

if __name__   == "__main__":
	wtype = input("Congrats on the workout. What type of workout was it? ")
	if 'un' in wtype:
		main1()	
	elif 'rg' in wtype:
		main2()
	else:
		main3()	
		
