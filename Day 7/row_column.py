import numpy as np
a=np.array([[1,2,3,4,5],
            [6,7,8,9,0]])
print(a)
#[row,columnn]
print(a.shape)

#get a specific row element [r,c]
output1=a[0, :] #0 row and all the column
print(output1)

#get a specific column
output2=a[:,2] #all the row and 2
print(output2)

#getting a little more fnacy [ start index:end index:step size]
print(a[0,:1:6])
