europe = {'spain': 'madrid', 'france':'paris','germany':'berlin' ,'norway':'oslo', 'australia':'vienna'}
europe['italy']='rome'
print(europe)

print(europe['italy']== 'rome')

europe['poland']='warsaw'

europe['germany']='berlon'
del(europe['australia'])
print(europe)

#Dictionaries part 2

#Dictionary opf Dictionaries
europe = {'spain': {'capital':'madrid', 'population': 46.77},
          'france': {'capital':'paris', 'population': 66.03},
          'germany': {'capital': 'berlin', 'population': 80.62},
          'norway': {'capital': 'oslo', 'population': 5.084}}
print(europe['france']['capital'])

#Create sub dictionary
data = {'capital':'rome', 'propulation':59.83}

europe['italy']=data

print(europe)