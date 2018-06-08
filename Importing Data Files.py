# Open a file: file
file = open('Demographic_Statistics_By_Zip_Code.csv', 'r')

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)
