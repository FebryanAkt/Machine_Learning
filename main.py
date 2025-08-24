import pandas as pd

data = 'Titanic-Dataset.csv' 
df = pd.read_csv(data)
print(df.head())