import pandas.io.json as pd_JSON

f=open("C:\\Users\\Kulraj\\Documents\\GitHub\\Data Engineering with Python\\Writing Files\\Files\\mycsv.csv",'r')

#Loading file with pandas version of JSON.loads():

data = pd_JSON.loads(f.read())

#To fit into table you need to normalize and flatten the JSON.
# Passing the records path because that is where our JSON lives

df = pd_JSON.json_normalize(data,record_path='records')

# Printing out Result
print(df.head(2).to_json())

# By changing the oreint value to records you get each row as a record in the JSON format
print(df.head(2).to_json(orient='records'))