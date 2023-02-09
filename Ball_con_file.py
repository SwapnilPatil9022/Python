# Ball casestudy application dataset write into new .xlsx file format.

# import required library
import pandas as pd

# Dataframe weigth, feature, label columns

df = pd.DataFrame({'Weigth' : [35,47,90,48,91,36,92,34,39,31,96,43,110,33,95],
				'Features' : ["Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Rough","Soft","Rough","Soft","Rough","Smooth"],
				'Labels' : ["Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket"]})


"""
df = pd.DataFrame({'Weigth' : [35,47,90,48,90,35,92,35,35,35,96,43,110,35,95,35,47,90,48,90,35,92,35,35,35,96,43,110,35,95,35,47,90,48,90,35,92,35,35,35,96,43,110,35,95,35,47,90,48,90,35,92,35,35,35,96,43,110,35,95,],
				'Features' : ["Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth","Rough","Rough","Rough","Smooth","Rough","Smooth","Rough","Smooth"],
				'Labels' : ["Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket","Tennis","Tennis","Tennis","Criket","Tennis","Criket","Tennis","Criket"]})
"""
# create a pandas excel write using XlsxWriter as the engine.
writer = pd.ExcelWriter('Ball_into_df1.xlsx', engine = 'xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name = 'Sheet1', index=False)

# Close the pandas excel.  writer and output the excel file.
writer.close()
 




