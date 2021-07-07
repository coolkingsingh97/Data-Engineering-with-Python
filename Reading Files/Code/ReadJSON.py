import json

## Opening File ##

with open("C:\\Users\\Kulraj\\Documents\\GitHub\\Data Engineering with Python\\Writing Files\\Files\\mycsv.csv","r") as f:
	data = json.load(f)


print(data['records'][434])