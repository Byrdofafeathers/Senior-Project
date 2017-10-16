import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.preprocessing import LabelEncoder

def open_data():
	info = pd.read_csv('Datasets/Pisa mean performance scores 2013 - 2015 Definition and Source.csv')
	db = pd.read_csv('Datasets/Pisa mean perfromance scores 2013 - 2015 Data.csv')
	return {"info": info, "db":db}
database = open_data()

# Pre - Processing 
database['db'] = database['db'].drop([1161, 1162, 1163, 1164, 1165]) # Removes Strangly Included DB information in rows
drop = ['..', 'VNM']
database['db'] = database['db'][~database['db']['2015 [YR2015]'].isin(drop)]

print(database['db']['Country Code'])
database['db']['Country Code Label'] = database['db']['Country Code'].astype('category').cat.codes



print(database['db'][['Country Code', 'Series Code', '2015 [YR2015]']])
ax = plt.xticks(database['db']['Country Code Label'], database['db']['Country Code'], rotation=70)

plt.scatter(database['db']['Country Code Label'], database['db']['2015 [YR2015]'])
plt.show()