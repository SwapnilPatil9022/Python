import pandas as pd
#from xlsxwriter import Workbook

df = pd.DataFrame({'Data' : [11,21,51,101,111,121],'Labels' : [111,221,251,1021,1211,1221]})

writer = pd.ExcelWriter('MarvellousPandas.xlsx')

df.to_excel(writer, sheet_name='Sheet1')

writer.save()