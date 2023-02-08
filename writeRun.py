#Ideal functionality for this will be to write every workout to a csv called allRuns.csv, and to write to best if the pace beats a PR

from runClass import *

def main():
	new = newRun()
	f = open("run.csv", "a")
	f.write( new.findName() + ' ,' + new.findType() + ' ,' + str(new.findDist()) + ' ,' + new.findPace() + ' ,' + new.findDate() + ' ,')
	f.close()
	
if  __name__ == "__main__":
	main()	


