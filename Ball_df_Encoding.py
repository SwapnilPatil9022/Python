# import required library
import pandas as pd
from sklearn import preprocessing

# Dataframe weigth, feature, label columns
Weigth = [35,47,90,48,90,35,92,35,35,35,96,43,110,35,95,35,47,90,48,90,35,92,35,35,35,96,43,110,35,95,35,47,90,48,90,35,92,35,35,35,96,43,110,35,95,35,47,90,48,90,35,92,35,35,35,96,43,110,35,95,]
Features = ["Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth"]
Labels = ["Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket"]

# Create labelEncoder
le = preprocessing.LabelEncoder()

# Converting string labels into numbers.
Weigth_encoder = le.fit_transform(Weigth)
print(Weigth_encoder)
print("-------------------------------------------------------------------------")

# Converting string labels into numbers.
Features_encoder = le.fit_transform(Features)
print(Features_encoder)
print("-------------------------------------------------------------------------")

# Converting string labels into numbers.
Labels_encoder = le.fit_transform(Labels)
print(Labels_encoder)
print("-------------------------------------------------------------------------")
