import pandas as pd
data= pd.DataFrame(pd.read_excel('数据大集成.xlsx','Sheet1'))
no_re_row = data.drop_duplicates()
print(no_re_row)
no_re_row.to_excel("新(数据大集成).xls")