#!/bin/bash

#Takes file to be searched as argument 1 and search term as argument 2

cat $1 | head -n1 > $2.csv && cat $1 | grep $2 >> temp.csv
cat temp.csv | sort -t, -n -k$3 -r >> $2.csv
rm -f temp.csv
open $2.csv
sleep 1
