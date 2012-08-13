#!/bin/bash

echo "Subject,Start Date" > all_games.csv

for i in `ls orka-?.html`;
do
	echo $i;
	cat $i | ./convert.py >> all_games.csv
done
