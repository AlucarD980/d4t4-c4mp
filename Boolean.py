import numpy as np

print(True==False)

print(-5*15 != 75)

print("pyscript" == "PyScript")

print(True == 1)

x = -3*6
print(x >= -10)

y = "test"

print("test" <= y)

#alphabetical order
print(True>False)

#creating arrays

my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

print(my_house>18)

print(my_house< your_house)

#logic operators array numpy
print(np.logical_or(my_house > 18.5, my_house < 10))

print(np.logical_and(my_house < 11, your_house < 11))


