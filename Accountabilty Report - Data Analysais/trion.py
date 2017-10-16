import pandas as pd 
import matplotlib.pyplot as plt 

def load_data():
	overall = pd.read_excel('Datasets/acctsumm16.xlsx')
	return {'acctsum': overall} 

db = load_data()
acctsum = db['acctsum']
print(acctsum.columns)
acctsum.set_index('School Code', verify_integrity=True)
drop = ['', ' ', '*', '>95', '<5']
acctsum = acctsum[~acctsum['Math I Percent College/Career Ready'].isin(drop)]
acctsum['District Name Code'] = acctsum['District Name'].astype('category').cat.codes
print(acctsum.dtypes)
plt.xticks(acctsum['District Name Code'], acctsum['District Name'], rotation=70, size=5)
plt.scatter(acctsum['District Name Code'], acctsum['Math I Percent College/Career Ready'].astype('Float64'))

plt.show()
plt.xlabel('School District')
plt.ylabel('Percent College/Carrer Ready in Math I')
print(acctsum.shape)