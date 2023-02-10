#!/bin/bash

#Takes file to be searched as argument 1 and search term as argument 2
#and the column to be sorted by (determined by new.search()) as argument 3
if  [[ "'$1'" == *lift* ]];
then
	cat $1 | head -n1 > "$2".csv && cat $1 | grep -i "$2" >> temp.csv
	cat temp.csv | sort -t, -n -k$3 -r >> "$2".csv
elif [[ "'$1'" == *erg* ]];
then
	cat $1 | head -n1 > "$2".csv && cat $1 | grep -i "$2" >> temp.csv
	cat temp.csv | sort -t, -n -k$3  >> "$2".csv
else
	cat $1 | head -n1 > "$2".csv && cat $1 | grep -i "$2" >> temp.csv
	cat temp.csv | sort -t, -n -k$3 -r  >> "$2".csv

fi
rm -f temp.csv
open "$2".csv
sleep 1
rm -f "$2".csv

