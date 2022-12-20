import pandas as pd
import matplotlib.pyplot as plt

excel_file = 'Marvellous.xlsx'
data = pd.read_excel(excel_file)

print("All data from excel file")
print(data)

print("First 5 rows from file")
print(data.head())

print("First 4 rows from file")
print(data.head(4))

print("Last 3 rows from file")
print(data.tail(3))

print("First 4 rows from file")
print(data.head(4))

print(data.shape)
print("------------------------------------------------")
Sorted_data = data.sort_values(['Name'], ascending=False)
print("Sorted_data")
print(Sorted_data)