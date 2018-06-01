#getting column area
#brics["area"]
#brics.iloc[:, "area"]
#bircs.iloc[:,2]
#condition over a column
# is_huge = brics["area"] < 8 == list
#Filter data frame
#brics[is_huge] == filtered dataframe
#or
#brics[brics["area"] > 8]

#logical - selecting areas > 8 and < 10

#np.logical_and(brics["area]> 8, bircs["area"] < 10) = Boolean series

#brics[np.logical_and(brics["area]> 8, bircs["area"] < 10)]

#use a boolean pandas series to subset

#dr = boolean pandas series

#sel = car[dr]dr =