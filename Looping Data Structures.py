# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe

for key, value in europe.items():
    print("the capital of " + key + " is " + value)


#Iterating over Dataframe

import pandas as pd
new_york_demo = pd.read_csv('Demographic_Statistics_By_Zip_Code.csv', index_col=0)
for lab,row in new_york_demo.itterrows():
   print(lab)
   print(row)




