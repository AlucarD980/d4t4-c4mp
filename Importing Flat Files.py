import numpy as np
import matplotlib.pyplot as plt

#Name of the file
file = 'Demographic_Statistics_By_Zip_Code.csv'

#Load it into an array
digits = np.loadtxt(file, delimiter=',', skiprows=1) #Skips first row

print(digits)

print(type(digits))

print(digits.shape)

#Reading with different separator

#data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=(0,2)) #Skips first row adn tab as separator, uses just column 1 and 3






