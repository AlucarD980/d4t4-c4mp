import numpy as np
import matplotlib.pyplot as plt

#Name of the file
file = 'Demographic_Statistics_By_Zip_Code.csv'

#Load it into an array
digits = np.loadtxt(file, delimiter=',', skiprows=1) #Skips first row

print(digits)

print(type(digits))

print(digits.shape)





