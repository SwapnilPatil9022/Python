import pandas as pd 

# print("Dataframe with list")
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)
print("----------------------")

# print("Dataframe with list")
data = [['PPA',4],['LB',3],['Python',3],['Anguler',3]]
df = pd.DataFrame(data, columns=['Name','Duration'])
print(df)
print("-----------------------")

data = {'Name' : ['PPA', 'LB', 'Python', 'Anguler', 'LSP'], 'Duratioon' : [4,3,3,3,5]}
df = pd.DataFrame(data)
print(df)
print("-----------------------")

data = [{'Name':'PPA','Duration':3,'Fees':10500},{'Name':'LB','Duration':4,'Fees':18000},{'Name':'Python','Duration':5,'Fees':18500}]
df = pd.DataFrame(data)
print(df)