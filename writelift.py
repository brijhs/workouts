from liftClass import *

def main3():
	new = newLift()
	f = open('lift.csv', 'a')
	f.write(new.getName() + ' ,' + str(new.getWeight()) + ' ,' + str(new.getReps()))
	f.close()

if __name__ == "__main__":
	main()
