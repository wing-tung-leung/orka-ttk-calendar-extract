#!/bin/bash

echo "Subject,Start Date" > all_junior_games.csv

for i in `ls junior-?.html`;
do
	cat $i | ./convert-junior.py >> all_junior_games.csv
done
