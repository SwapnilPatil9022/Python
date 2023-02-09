# Ball_info_df.xlsx file format to display the using matplotlib library and Save scatter plot in graph in current folder.

import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt
import seaborn as sns

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

plt.scatter(features,weigth, color="b")
plt.plot(features,weigth, color="r")
plt.title("Ball_Predictor_CaseStudy")
plt.xlabel("weigth")
plt.ylabel("Surface")
plt.plot(features,weigth, color="r")
plt.savefig('C:/python/Ball_df_Graph.png', transparent=False, bbox_inches='tight')
plt.show()

