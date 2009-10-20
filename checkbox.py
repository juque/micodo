#!/usr/bin/env python
import csv
import sys
CAMPOS = "dbs/checkbox.csv"
PLANTILLA = "plantillas/checkbox.txt";

campos = open(CAMPOS,"r")
plantilla = open(PLANTILLA,"r")

csv_reader = csv.reader(campos)
template = plantilla.read()

for row in csv_reader:
	 campo1 = row[0]
	 campo2 = row[1]
	 campo3 = row[2]
	 campo4 = row[3]
	 res = template.replace("$C1$",campo1)
	 res = res.replace("$C2$",campo2)
	 res = res.replace("$C3$",campo3)
	 res = res.replace("$C4$",campo4)
	 print res,
