from urllib.request import urlretrieve
import pandas as pd
url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
urlretrieve(url, 'winequality.csv')

df = pd.read_csv('winequality.csv', sep = ';')
print(df.head())