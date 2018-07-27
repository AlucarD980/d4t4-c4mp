import pandas as pd

file = 'titanic.csv'

df = pd.read_csv(file)

print(df.head) #Print headers