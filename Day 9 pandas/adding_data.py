import pandas as pd

df=pd.read_csv('D:/90 days AI Ml/Day 9 pandas/pokemon_data.csv')
#df['Total']=df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
#df=df.drop(columns='Total')

df['Total'] = df.iloc[:,4:10].sum(axis=1)
cols=list(df.columns.values)
df=df[cols[0:4]+[cols[-1]]+cols[4:12]]

#df.to_csv('D:/90 days AI Ml/Day 9 pandas/modifiedcsv.csv',index=False)
#df.to_excel('D:/90 days AI Ml/Day 9 pandas/modifiedexcel.xlsx', index=False)
df.to_csv('D:/90 days AI Ml/Day 9 pandas/modifiedtext.txt',index=False,sep='\t')