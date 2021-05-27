import pandas as pd

data_file = './data/leveranciers.xlsx'                                  # the input excel file

output_file_1 = './data/week1.csv'                                      # the name of first output file
output_file_2 = './data/week2.csv'                                      # the name of second output file
output_file_3 = './data/week3.csv'                                      # the name of third output file

def get_dax_for_week(data_file, output_file, columns, date):

        df = pd.read_excel(data_file, usecols=columns)                  # read the columns from the data_file
        df.columns = [c.split('.')[0] for c in df.columns]              # the magazijn columns appear multiple times, with .1, .2 postfix, remove that postfix
        
        df2 = df.melt(id_vars=["IGNR", "LEV NR", "Haven"],              # get the magazijn in rows
                var_name="Magazijn", 
                value_name="Aantal")

        
        df3 = df2[['Magazijn', 'IGNR', 'Aantal', 'LEV NR', 'Haven']]    # select the correct columns for DAX
        df3.columns = ['Magazijn', 'Artikel', 'Aantal', 'leveranciersnummer', 'Haven']  # rename columns to DAX format
        datumcol = [date for x in range(len(df3.index))]
        df3.insert(2, "Datum", datumcol)
        df3.to_csv(output_file, sep='|', index=False)                           # write to csv file

get_dax_for_week(data_file, output_file_1, "A,D,F,G:I", "week33")               # create csv for first week (magazijn G:I)
get_dax_for_week(data_file, output_file_2, "A,D,F,J:L", "week40")               # create csv for second week (magazijn J:L)
get_dax_for_week(data_file, output_file_3, "A,D,F,M:O", "week45")               # create csv for third week (magazijn m:o)