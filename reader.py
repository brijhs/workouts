import csv
from runClass import *
paceFind(run):
	with open('bests.csv') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		for row in csv_reader:
			if row['name'] == run.findName():
				if floatPace(row['Pace']) > floatPace(run.findPace()):
				#Need to read the entire file in, set up an if conditional if the name (must be saved in this if) matches the name in a given line, rewrite that line somehow, and spit it back out
