#Pandaaaaas

import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap':cpc}

print(my_dict)

cars = pd.DataFrame(my_dict)

print(cars)
row_labels = ['US', 'AU', 'JP', 'IN', 'RU', 'MO', 'EG']

cars.index = row_labels

print(cars)

#import csv to pandas
#index_col avoids automatic Index and takes first column as Index

new_york_demo = pd.read_csv('Demographic_Statistics_By_Zip_Code.csv', index_col=0)

print(new_york_demo)

print(new_york_demo.loc[1:3,['COUNT PARTICIPANTS']])
