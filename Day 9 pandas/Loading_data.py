import pandas as pd

#df=pd.read_csv('D:\90 days AI Ml\Day 9\pokemon_data.csv')
#print(df.head(3)) #top 3 rows

#df_xlsx =pd.read_excel('D:/90 days AI Ml/Day 9/pokemon_data.xlsx') #using forward slash because it confuse the escape sequence 9\
#print(df_xlsx.head(3))

df=pd.read_csv('D:/90 days AI Ml/Day 9 pandas/pokemon_data.txt',delimiter='\t')
print(df.head(5))