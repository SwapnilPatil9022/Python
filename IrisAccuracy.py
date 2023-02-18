"""
    -------------------Supervised Machine Learning----------------------------
        ----Accuracy Calculation with Decision Tree & K Nearest Neighbour-----
    * In this application we train iris data set with Decision Tree algorithem and K Nearest Neighbour algorithm.
    * We divide iris data set into two equal part as tranning data and test data.
    * We applay tranning on tranning data and predict the result on test data.
    * We calculate accuracy of both the algorithems by applaying of test data.

    - Consider below characteristics of Machine Learning Application:
        Classifire :    Decision Tree & K Nearest Neighbour
        DataSet :       Iris Dataset
        Features :      Sepal Width, Sepal Length, Petal Width, Petal Length
        Labels :        Versicolor, Sentosa, Virginica
        Tranning Dataset :      75 Entries
        Testing Dataset :       75 Entries
"""
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def MarvellousCalculateAccuracyDecisionTree():
    iris = load_iris()

    data = iris.data
    target = iris.target

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
