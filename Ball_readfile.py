# Read the data from Ball_into_df.xlsx file.

import pandas as pd 
import matplotlib.pyplot as plt

excel_file = 'Ball_into_df.xlsx'
batches = pd.read_excel(excel_file, sheet_name = 0, index_col=0)

print(batches.head(10))
print("---------------------------")
print(len(batches))



