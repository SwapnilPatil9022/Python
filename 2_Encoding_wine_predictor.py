# Read the data and encoding the data from Wine_Predictor.xlsx file.

import pandas as pd 
from sklearn import tree
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
import seaborn as sns
#import plotly.express as px
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

excel_file = 'WinePredictor.xlsx'
data = pd.read_excel(excel_file, sheet_name = 0, index_col=0)

print("Rows,columns:",(data.shape))
print(data.head())

print(data.isna().sum())

#fig = plt.scatter(data,x='quality')
#fig.show()

corr = data.corr()
plt.subplots(figsize=(15,10))
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True, cmap=sns.diverging_palette(220,20, as_camp=True))





"""



	target = data.Class

	print(data.head(10))
	print("Size of actual dataset is :",len(data))

	data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.5)

	classifier = tree.DecisionTreeClassifier()

	classifier.fit(data_train,target_train)

	predictions = classifier.predict(data_test)

	Accuracy = accuracy_score(target_test, predictions)

	return Accuracy

def MarvellousCalculateAccuracyKNeighbour():
    iris = load_iris()

    data = iris.data
    target = iris.target

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.5)

    classifier = KNeighborsClassifier()

    classifier.fit(data_train, target_train)

    predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test, predictions)

    return Accuracy

def main():
    Accuracy = MarvellousCalculateAccuracyDecisionTree()
    print("Tree",Accuracy*100,"%")

    Accuracy = MarvellousCalculateAccuracyKNeighbour()
    print("KNN",Accuracy*100,"%")

if __name__ == "__main__":
    main()
"""