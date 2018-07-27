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

#Import data as floats and skip the first row: data_float dtype=str
#data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)


#-------------------------------------#
#Data set with multiple data types
#np.genfromtxt is an structured array handling umutiple data types.


#data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None)
#print(data.dtype.names)
#data[i] call to rows
#data['Column'] call to  columns


#------------------------------------#
#np.recfromcsv has none type and , as default separator
# Assign the filename: file
#file = 'titanic.csv'

# Import file using np.recfromcsv: d
#d = np.recfromcsv(file)

# Print out first three entries of d
#print(d[:3])

