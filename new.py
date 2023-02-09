from writeRun import *
from writeerg import *
from writelift import *
import os
import sys

def newWorkout():
	wtype = input("Congrats on the workout. What type of workout was it? ")
	if 'un' in wtype:
		main1()	
	elif 'rg' in wtype:
		main2()
	else:
		main3()	

def search():
	file = input("Run, erg, or lift? ")
	term = input("Which {}? ".format(file))
	file = file + '.csv'
	os.system('sh search.sh {} {}'.format(file, term))
if __name__   == "__main__":
	choice = input('Would you like to log a new workout or search existing ones? ')
	if 'earch' in choice:
		search()
	else:
		newWorkout() 
		
	
		
