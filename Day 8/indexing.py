#advance indexing
#boolean masking and advance indexing
import numpy as np
file_data=np.genfromtxt('D:\90 days AI Ml\Day 8\data.txt',delimiter=',')
filedata=file_data.astype('int32')
print(filedata>50)
print(filedata[filedata>=50])

#you can index with a list in numpy
a=np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,8]]) #ayy list ma index ho for eg index 0 = 1 index 1=2

#any value form the column is greater than 50
z=np.any(filedata>50,axis=0)
print(z)

m=np.all(filedata>50,axis=0)
print(m)
p=((filedata>50) & (filedata<100))
print(p)

#we can do reverse
r=(~((filedata>50) & (filedata<100)))
print(r)

