from faker import Faker
import csv


## Open file ##

output = open("C:\\Users\\Kulraj\\Documents\\GitHub\\Data Engineering with Python\\Writing Files\\Files\\data.csv",mode = "w")

## Create callable object of Faker ##
fake = Faker()

## Creating Headers ##

header = ['name','age','street','city','state','zip','lng','lat']

## Create CSV Writer ##

mywriter = csv.writer(output)

## Adding Header ##

mywriter.writerow(header)

## Adding Fake Data ##

for r in range(1000):
	mywriter.writerow([fake.name(),fake.random_int(min=18,max=80,step=1),fake.street_address(),fake.city(),fake.state(),fake.zipcode(),fake.longitude(),fake.latitude()])

## Closing File ##

output.close()

