# # Section 1
import pandas as pd

data_file = './data/leveranciers.xlsx'

df = pd.read_excel(data_file , usecols="A,D,F,J:R")
# print(df.to_markdown())

df2 = df.melt(id_vars=["IGNR", "LEV NR", "Haven"], 
        var_name="Magazijn", 
        value_name="Aantal")

print(df2)

df3 = df2[['Magazijn', 'IGNR', 'Aantal', 'LEV NR', 'Haven']]
df3.columns = ['Magazijn', 'Artikel', 'Aantal', 'leveranciersnummer', 'Haven']
df3.to_csv('new_file.csv', sep='|', index=False)