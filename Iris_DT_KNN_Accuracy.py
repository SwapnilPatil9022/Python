




























"""
    -------------------- Supervised Machine Learning -------------------------
    ------------- Accuracy Calculation with Decision Tree --------------------
                                    &
    ------------------------ K Nearest Neighbour -----------------------------

    * In this application we train iris data set with Decision Tree algoritham and k Nearest Neighbour algoritham
    * We divide iris data set into two equal as training data and test data.
    * We apply training on training data and predict the data result on test data.
    * We calculate accuracy of both the algorithams by applaying of test data.

    - Consider below characteristics of machine learning application : 

    classifier      : Decision Tree & K Nearst Neighbour
    Dataset         : Iris Dataset
    Features        : Sepal Width, Sepal length, petal Width, petal Length
    Labels          : Versicolor , setosa , Virginica   
    Traning Dataset :  75 Enteris
    Testing Datset  :  75 Enteris
    ------------------------------------------------------------------------
"""
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

    data_train, data_test, target_train, target_test = train_test_split(data,target,test_size = 0.5)

    # Using DecisionTree algoritham
    classifier = tree.DecisionTreeClassifier()

    classifier.fit(data_train,target_train)

    Predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test, Predictions)

    return Accuracy
 
def MarvellousCalculateAccuracyKNeighbor():
    iris = load_iris()

    data = iris.data
    target = iris.target

    data_train, data_test, target_train, target_test = train_test_split(data,target,test_size = 0.5)

    # Using KNN algoritham
    classifier = KNeighborsClassifier()

    classifier.fit(data_train,target_train)

    Predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test, Predictions)

    return Accuracy

def main():
    Accuracy = MarvellousCalculateAccuracyDecisionTree()
    print("Accuracy of classification algorithm with Decision Tree classifier is :",Accuracy*100,"%d")

    Accuracy = MarvellousCalculateAccuracyKNeighbor()
    print("Accuracy of classification algorithm with K Neighbour classifier is :",Accuracy*100,"%d")

if __name__ == "__main__":
    main()

"""