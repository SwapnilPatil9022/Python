import pandas as pd
import numpy as np

data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s[0])
print("----------------------------------")

# Costomize indexing 
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,200,300,400])
print(s[300])
print("----------------------------------")

data = {'a' : 0.1, 'b' : 0.2, 'c' : 0.3}
s = pd.Series(data)
print(s)
print("----------------------------------")

s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s['c'])