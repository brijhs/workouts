#!/bin/bash

#Takes file to be searched as argument 1 and search term as argument 2

cat $1 | head -n1 > $2.csv && cat $1 | grep $2 >> $2.csv

open $2.csv
done
