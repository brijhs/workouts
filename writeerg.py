from ergClass import *

def main2():
	new = newErg()
	f = open('erg.csv', 'a')
	f.write(new.getName() + ' ,' + new.getSplits() +' ,')
	f.close()

if __name__ == '__main__':
	main2()
