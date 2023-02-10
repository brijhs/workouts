#Ideal functionality for this will be to write every workout to a csv called allRuns.csv, and to write to best if the pace beats a PR

from runClass import *
import sys
import os

def main1():
	new = newRun()
	f = open("run.csv", "a")
	f.write( new.findName() + ' ,' + new.findType() + ' ,' + str(new.findDist()) + ' ,' + new.findPace() + ' ,' + new.findDate() + '\n')
	f.close()
	print("Let's see how this stacks up with the rest of your efforts...")
	os.system('sh search.sh {} {} {}'.format("run.csv", "'" + new.findName() + "'", 4))
	
if  __name__ == "__main__":
	main1()	


