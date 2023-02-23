"""
        ----------------------Supervised Machine Learning-----------------------------
            --------User Defined K Nearest Neighbour Algoritham-----------
    ----------------------------------------------------------------------------------------
    * In this application we create our own algoritham for classified machine learning.
    * We create our own K Nearest Neighbour algoritham.
    * For user defined algoritham we design one class named as MarvellousKNN.
    * This class contains 3 methoads as fit, predict, closest method.
    * There is one naked method euc() which calculate distance between two points using 
        Eucclidean distance algorithm.
    * fit() method initialise traning data and its targets iniside class.
    * predict() method creates one array as prediction which store stortest distance between
        all test data and traning data elements.
    * predict() method calls closest methoad ehich returns tyhe shortest distance.
  ---------------------------------------------------------------------------------------------
 - Consider below characteristics of Machine Learning Application :
        
        Classifire :         User defined K Nearest Neighbour
        DataSet :            Iris Dataset
        Features :           Sepal Width, Sepal Length, Petal Width, Petal Length
        Labels :             Versicolor, Sentosa, Virginica
        Tranning Dataset :      75 Entries
        Testing Dataset :       75 Entries
"""
from sklearn import tree
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def euc(a,b):
    return distance.euclidean(a,b)

class MarvellousKNN():
    def fit(self,TranningData,TranningTarget):
        self.TranningData = TranningData
        self.TranningTarget = TranningTarget

    def predict(self,TestData):
        predictions = []
        for row in TestData:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self, row):
        bestdistance = euc(row, self.TranningData[0])
        bestindex = 0
        for i in range(1,len(self.TranningData)):
            dist = euc(row,self.TranningData[i])
            if dist < bestdistance:
                bestdistance = dist
                bestindex = i   
        return self.TranningTarget[bestindex]

def MarvellousKNeighbor():
    border = "-"*50

    iris = load_iris()

    data = iris.data
    target = iris.target

    print(border)
    print("Actual data set")
    print(border)

    for i in range(len(iris.target)):
        print("ID : %d,Label %s, Feature : %s"%(i,iris.data[i],iris.target[i]))
    print("Size of Actual data set %d"%(i+1))

    data_train, data_test, target_train, target_test = train_test_split(data,target, test_size = 0.5)

    print(border)
    print("Tranning data set")
    print(border)

    for i in range(len(data_train)):
        print("ID : %d,Label %s,Feature : %s"%(i,data_train[i],target_train[i]))
    print("Size of Traning data set %d"%(i+1))

    print(border)
    print("Test data set")
    print(border)

    for i in range(len(data_test)):
        print("ID : %d,Label %s, Feature : %s"%(i,data_test[i],target_test[i]))
    print("Size of Test data set %d"%(i+1))
    print(border)

    classifier = MarvellousKNN()

    classifier.fit(data_train,target_train)

    predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test, predictions)

    return Accuracy

def main():

    Accuracy = MarvellousKNeighbor()
    print("Accuracy of classification algoritham with K Neighbor classifier is",Accuracy*100,"%")

if __name__ == "__main__":
    main()
