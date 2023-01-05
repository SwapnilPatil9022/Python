# Read the data from Wine_Predictor.xlsx file.

import pandas as pd 

excel_file = 'WinePredictor.xlsx'
data = pd.read_excel(excel_file, sheet_name = 0, index_col=0)

print(data.head(10))