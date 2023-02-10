from ergClass import *
import sys 
import os

def main2():
	new = newErg()
	f = open('erg.csv', 'a')
	f.write(new.getName() + ' ,' + new.getSplits() +' ,' + new.getDate() + '\n')
	f.close()
	print("Let's see how this stacks up with the rest of your efforts...")
	os.system('sh search.sh {} {} {}'.format("erg.csv", "'" + new.getName() + "'", 4))

if __name__ == '__main__':
	main2()
