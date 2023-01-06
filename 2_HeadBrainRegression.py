"""
        =================== Machine Learning Application===================
        -------------------Supervised Machine Learning---------------------
        -----------------------Linear Regression---------------------------
        -------------------------------------------------------------------
        Classifier :        Linear Regression
        DataSet :           Head Brain Dataset
        Features :          Gender, Age, Head size, Brain weight
        label :             -
        Tranning Dataset :  237
        ------------------------------------------------------------------
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def HeadBrainPredictor():

    # Load data
    data = pd.read_csv("HeadBrain.csv")

    print("Size of data set is :",data.shape)

    X = data['Head Size(cm^3)'].values
    Y = data['Brain Weight(grams)'].values

    X = X.reshape((-1,1))

    n = len(X)

    reg = LinearRegression()

    reg = reg.fit(X,Y)

    y_pred = reg.predict(X)

    r2 = reg.score(X,Y)

    print("Goodness of fit is : ",r2)

def main():
    print("----------HeadBrain CaseStudy by Swapnil Patil----------")

    print("--------------Supervised Machine Learning---------------")

    print("----Linear Regreesion on Head and Brain size data set---")
    print("--------------------------------------------------------")

    HeadBrainPredictor()

if __name__ == "__main__":
    main()

