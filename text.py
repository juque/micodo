#!/usr/bin/env python
import csv
import sys
CAMPOS = "dbs/text.csv"
PLANTILLA = "plantillas/text.txt";

campos = open(CAMPOS,"r")
plantilla = open(PLANTILLA,"r")

csv_reader = csv.reader(campos)
template = plantilla.read()

for row in csv_reader:
	 campo1 = row[0]
	 campo2 = row[1]
	 res = template.replace("$C1$",campo1)
	 res = res.replace("$C2$",campo2)
	 print res,
