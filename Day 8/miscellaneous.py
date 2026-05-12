import numpy as np
#load data from files
file_data=np.genfromtxt('D:\90 days AI Ml\Day 8\data.txt',delimiter=',')
print(file_data) #auto float
filedata=file_data.astype('int32')
print(filedata)

