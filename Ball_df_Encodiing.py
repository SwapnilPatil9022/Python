# This application is converting the .xlsx file string data into integer values (Encoding)

import pandas as pd
from sklearn import preprocessing

excel_file = 'Ball_into_df.xlsx'
data = pd.read_excel(excel_file)

print("Size of actual dataset is :",len(data))

feature_names = ['Weigth','Features','Labels']

print("Names of Features", feature_names)
print("-------------------------------------------------------------")

weigth = data.Weigth
features = data.Features
labels = data.Labels

le = preprocessing.LabelEncoder()

weigth_encoded = le.fit_transform(features)
print(weigth_encoded)
print("-------------------------------------------------------------")

features_encoded = le.fit_transform(weigth)
print(features_encoded)
print("-------------------------------------------------------------")

labels_encoded = le.fit_transform(labels)
print(labels_encoded)
print("-------------------------------------------------------------")

