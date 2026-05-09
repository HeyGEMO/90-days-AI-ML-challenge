import numpy as np

#list slow
#numpy fast
#numpy use fixed type
a = np.array([1,2,3])
#a = np.array([1,2,3],dtype='int16')
print(a)
b=np.array([[4.0,5.0,6.0],       
            [7.0,8.0,9.0]
            ])
print(b)

#get dimension
print(a.ndim) #1
#get shape #(3, )
print(a.shape)

#get type
print(a.dtype) #int32 change to int16
#get size
print(a.itemsize)
#get total size
print(a.size * a.itemsize) #same
print(a.nbytes)            #same
print(b.itemsize)
