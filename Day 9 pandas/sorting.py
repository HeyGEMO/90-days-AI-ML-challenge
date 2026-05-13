#sorting/describing data
import pandas as pd
df=pd.read_csv('D:/90 days AI Ml/Day 9 pandas/pokemon_data.txt',delimiter='\t')
#print(df.describe()) #give high level stats like mean standard deviation like stats

print(df.sort_values('Name'))
#decending
print(df.sort_values('Name',ascending=False))

#two values sorting
print(df.sort_values(['Type 1','HP'],ascending=[1,0])) #frist one is ascending and 2nd one is descending
