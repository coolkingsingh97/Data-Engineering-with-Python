import csv

## Opening a file ##

with open("C:\\Users\\Kulraj\\Documents\\GitHub\\Data Engineering with Python\\Writing Files\\Files\\data.csv") as f:


	## Creating Reader ##

	myreader = csv.DictReader (f)

	## Assigning Header ##

	headers = next(myreader)

	## Iterating through all the rows ##
	for row in myreader:
		print(row['name'])