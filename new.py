from writeRun import *
from writeerg import *
from writelift import *
import os
import sys

def newWorkout():
	wtype = input("Congrats on the workout. What type (run, erg, or lift) of workout was it? ")
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
	if 'a' in term or 'l' in term:
		os.system('open {}'.format(file))
	else:
		term = "'" + term + "'"
		if 'un' in file: 
			colval = 4
		else:
			colval = 2
		os.system('sh search.sh {} {} {}'.format(file, term, colval))
if __name__   == "__main__":
	choice = input('Would you like to log a new workout or search existing ones? ')
	if 'earch' in choice:
		search()
	else:
		newWorkout() 
		
	
		
