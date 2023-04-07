import pandas as pd


file = pd.read_excel(f'D:/DSFiles/bk/data/ahuizong.xlsx',
                     names=['district', 'mean', 'std', 'max', 'min', 'median'])  # encoding="GBK", encoding="utf-8",

print(file.round(2))

#print(file)

