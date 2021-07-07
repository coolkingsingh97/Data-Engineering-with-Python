from faker import Faker
import json

## Opening File ##

output = open("C:\\Users\\Kulraj\\Documents\\GitHub\\Data Engineering with Python\\Writing Files\\Files\\mycsv.csv","w")

fake = Faker()

## Initialize dictionary ##

alldata = {}

## Initialize key records ##
alldata['records'] = []

for x in range(1000):
	data = {"name":fake.name(),"age":fake.random_int(min=18,max=80,step=1),"street":fake.street_address(),"city":fake.city(),"state":fake.state(),"zip":fake.zipcode(),"lng":float(fake.longitude()),"lat":float(fake.latitude())}
	alldata['records'].append(data)

## Writing to JSON File ##

json.dump(alldata,output)

output.close()