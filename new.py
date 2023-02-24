
# import librarys
import pandas as pd
from sklearn import tree

# Load the dataset
# Rough 1
# Smooth 0

# Tennis 1
# Cricet 2

Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

# Deside the MAchine learnig algoritham
obj = tree.DecisionTreeClassifier()

# Perform the trenning model
obj = obj.fit(Features,Labels)

# perform the testing 
print(obj.predict([[97,0]])