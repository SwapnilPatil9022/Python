"""
	Consider below characteristics of machine learning application : 

	Classifier:		Decisuon Tree
"""

import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris

iris = load_iris()

print("Freature names of iris data set")
print(iris.feature_names)

print("Target names of iris data set")
print(iris.target_names)

#Indices of removed element
test_index = [1,51,101]

# Trenning data with removed elements
train_target = np.delete(iris.target,test_index)
train_data = np.delete(iris.data,test_index,axis=0)

#Testing data for testing on tranning data
test_target = iris.target[test_index]
test_data = iris.data[test_index]

#from decision tree classifire
classifire = tree.DecisionTreeClassifier()

#Apllay traning data to from tree
classifire.fit(train_data, train_target)

print("Values that ew removed for testing ")
print(test_target)

print("Result is testing")
print(classifire.predict(test_data))