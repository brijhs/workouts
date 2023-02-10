from liftClass import *
import sys
import os

def main3():
	new = newLift()
	f = open('lift.csv', 'a')
	f.write(new.getName() + ' ,' + str(new.getWeight()) + ' ,' + str(new.getReps()) + ' ,' + new.getDate() + '\n')
	f.close()
	print("Let's see how this stacks up with the rest of your efforts...")
	os.system('sh search.sh {} {} {}'.format("lift.csv", "'" + new.getName() + "'", 4))
if __name__ == "__main__":
	main3()
