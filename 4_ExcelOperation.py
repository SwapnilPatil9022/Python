import pandas as pd

excel_file = 'Marvellous.xlsx'
batches = pd.read_excel(excel_file)

print(batches.head())
print("-------------------------------------------------")

batches_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
print(batches_sheet1.head()) 