
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset using pandas library
df = pd.read_csv('Diwali_Sales_Data.csv', encoding= 'unicode_escape')
print(df)
print("----------------------------------------------------")
df.shape
print(df)
print("----------------------------------------------------")
df.head(10)
print(df)
print("----------------------------------------------------")
df.info()
print(df)
print("----------------------------------------------------")

# Drop unrelated / blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace = True)
print(df)
print("==============================")

# Check for null values
pd.isnull(df).sum()
print(df)
print("==============================")

df.dropna(inplace = True)
print(df)
print("==============================")

# change data type
df['Amount'] = df['Amount'].astype('int')
print(df['Amount'].dtypes)
print("==============================")

# change the column name
df1 = df.rename(columns = {'Marital_Status':'Shaadi'})
print(df1.columns)
print("==============================")

# describe( method return description of the data in the DataFrame ( i.e Count, mean, std, etc))
print(df.describe())
print("==============================")

# Use describe() for specific columns
Sp = df[['Age','Orders','Amount']].describe()
print(Sp)
print("------------------------------------------------------------")

###########################################
# EXPLORATORY DATA ANALYSIS

print(df.columns)
print("==============================")

# display Gender column using matplotlib
gender_counts = df['Gender'].value_counts() 
plt.bar(gender_counts.index, gender_counts.values,  color = 'blue')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()
print("==============================")

ax = sns.countplot(x = 'Gender', data = df)

# Display bar chart with counts of male and female.
for i,count in enumerate(gender_counts.values):
    plt.text(i, count + 0.1, str(count), ha='center', va='bottom')
    # ax.bar_label(bars)

plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Count of Gender')
plt.show()
print("==============================")

# Display selse bar chart with counts of male and female.
Age_g = df['Age Group'].value_counts()
for i,count in enumerate(Age_g.values):
    plt.text(i, count + 0.1, str(count), ha='center', va='bottom')
    # ax.bar_label(bars)

plt.bar(Age_g.index, Age_g.values)
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.show()

print("==============================")

State = df['State'].value_counts() 
plt.bar(State.index, State.values)
plt.xlabel('State')
plt.ylabel('Order')
plt.show()

print("==============================")

# display Gender column using matplotlib
Status = df['Marital_Status'].value_counts() 
plt.bar(Status.index, Status.values,  color = 'blue')
plt.xlabel('Status')
plt.ylabel('Count')
plt.show()

print("==============================")

