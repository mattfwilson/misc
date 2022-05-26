import pandas as pd

excel_names = 'unclean_data.xlsx'
test = pd.read_excel(excel_names)

for column in test.columns:
    test[column] = test[column].str.replace(r'\W',"")
print(test)

