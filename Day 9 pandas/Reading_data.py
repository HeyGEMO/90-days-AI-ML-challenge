import pandas as pd
df=pd.read_csv('D:/90 days AI Ml/Day 9 pandas/pokemon_data.txt',delimiter='\t')
#print(df.columns) #read headers
#print(df['Name']) #read each column

#read each row
print(df.head(4)) #first 4 rows
print(df.iloc[1]) #everything in first row
print(df.iloc[1:4]) #one to four row
#for index,row in df.iterrows(): #itterate through rows
#    print(index,row['Name']) #row by row

#df.loc[df['Type 1']==['Fire']]

#read specific location (R,C)
print(df.iloc[2,1]) #2nd row and first column
