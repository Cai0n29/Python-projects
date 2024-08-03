import pandas as pd
from urllib.request import urlretrieve

print('Import flat files from the web to csv in Python')
print('Kindly input the url')

url = input()
print('Kindly input the name you wanted for the csv file')
csv = input()
file = csv+'.csv'
urlretrieve(url, file)
df = pd.read_csv(file, sep = ';')
print(df.head())
