import pandas as pd
import numpy as np
import json
import os
import shutil

print("Please make sure the table is in the same directory!")

path = input("Please enter the table's name: ")

if not os.path.exists(path):
    print("The Path entered does not exist!! Please check the Path again!)
    raise MyError()
          
df = pd.read_excel(path, header=None, skiprows=165)
df_NE = df[(df[1] == "NE_Accuracy") & (df[0] != "1")]
df_NE = df_NE.iloc[:, 2:]
df_NE['region'] = df.iloc[[idx + 1 for idx in df_NE.index]][0].apply(lambda x: x.split()[-1]).values
df_NE = df_NE.rename(columns = {2: "Unstandardized Coefficients B", 3: "Unstandardized Coefficients Std. Error", 4: "Standardized Coefficients Beta", 5: "t", 6: "Sig."})
df_NE = df_NE.set_index("region")
          
print("Table is extracted successfully!")

table_name = input("Now please enter the table's name you want: ")
df_NE.to_csv(table_name)