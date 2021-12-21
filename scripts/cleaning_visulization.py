import pandas as pd
import re
import numpy as np
from datetime import datetime
from dateutil.parser import parse
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('max_columns',None)

### Read the dataframe 
data=pd.read_csv('/Users/richardgil/Documents/BGSE/stats/finalproyect-stats/data/subset_data.csv')

### Handling Size of the app 
data['Size'].value_counts()
data['size_number']=[np.nan if len(re.findall(r'\d*\.?\d+',i))==0 else float(re.findall(r'\d*\.?\d+',i)[0]) for i in data['Size']]
data['size_units']=[np.nan if len(re.findall(r'\d*\.?\d+',i))==0 else re.findall(r'[a-zA-Z]+',i)[0] for i in data['Size']]
data['size_norm']=[i*0.001 if j=='k' else i for i,j in zip(data['size_number'],data['size_units'])]

### Handling the version of the app 
data['version']=[np.nan if i!=i else np.nan if len(re.findall(r'\d*\.?\d+',i))==0 else float(re.findall(r'\d*\.?\d+',i)[0]) for i in data['Minimum Android']]  

### Calculating Time Variables 
### Parsing string to dates
data['Released_1']=[np.nan if i!=i else parse(i) for i in data['Released']]
data['Last_Updated_1']=[np.nan if i!=i else parse(i) for i in data['Last Updated']]
data['Scraped_Time_1']=[np.nan if i!=i else parse(i) for i in data['Scraped Time']]
### days since realise 
data['time_realise']=[(i-j).days for i,j in zip(data['Scraped_Time_1'],data['Released_1'])]
### days since last update 
data['time_updated']=[(i-j).days for i,j in zip(data['Scraped_Time_1'],data['Last_Updated_1'])]
### days from realise to last update 
data['time_realise_update']=[-(i-j) for i,j in zip(data['time_updated'],data['time_realise'])]

### Drop auxiliar variables
data=data.drop(['Unnamed: 0','Unnamed: 0.1','Installs','Minimum Installs','Currency','Size','Minimum Android','Released','Last Updated','Scraped Time','size_units','size_number','Released_1','Last_Updated_1','Scraped_Time_1'],axis=1)
### Visulization 
### Continuos Variables
cont=['Rating','Rating Count','Maximum Installs','Price','size_norm','version','time_realise','time_updated','time_realise_update']
cat=['Category','Free','Content Rating','Ad Supported','In App Purchases','Editors Choice','Big_Category2']
keys=['App Name','App Id','Developer Id','Developer Website','Developer Email','Privacy Policy']

data[keys].head()

### Continuos Visualization 
for i in cont:
  sns.boxplot(x=data[i])
  plt.title(i)
  plt.xlabel(i)
  plt.show()