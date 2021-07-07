import csv

## Open a file in writing mode ##

output = open("C:\\Users\\Kulraj\\Documents\\GitHub\\Data Engineering with Python\\Writing Files\\Files\\mycsv.csv",mode = "w")


## Create a CSV writer ##

mywriter = csv.writer(output)

## Creating headers ##

header = ['name','age']

mywriter.writerow(header)

## Adding data ##

data = ['John Snow', 40]

mywriter.writerow(data)

output.close()
