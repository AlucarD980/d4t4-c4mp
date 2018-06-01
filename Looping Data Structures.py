# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe

for key, value in europe.items():
    print("the capital of " + key + " is " + value)


#Iterating over Dataframe
#Printing labels and each row as a series
import pandas as pd
new_york_demo = pd.read_csv('Demographic_Statistics_By_Zip_Code.csv', index_col=0)
for lab,row in new_york_demo.iterrows():
   print(lab)
   print(row)

#Iterate and Print a specific column
#itter does create a new pandas series on each iteration == INEFFICIENT
for lab, row in new_york_demo.iterrows() :
    print(str(lab)+": "+ str(row['COUNT GENDER TOTAL']))

#Adding a new calculated column and appying a function
for lab, row in new_york_demo.iterrows():
    new_york_demo.loc[lab, "count_gender_total"] = row['COUNT GENDER TOTAL']/2
print(new_york_demo)


#Using apply function - be careful with methods and functions
new_york_demo["Percent Gender Total"] = new_york_demo['PERCENT GENDER TOTAL']/2

#new_york_demo["Percent Gender Total"] = new_york_demo['PERCENT GENDER TOTAL'].apply(some function)
