#all 0s matrix
import numpy as np
a=np.zeros((2,3))
print(a)
b=np.ones((4,2,2),dtype='int32')
print(b)

#any other number
c=np.full((2,2),99)
print(c)

#any other number (full_like)
d=np.full(a.shape,4)
print(d)
d=np.full_like(a,4)
print(d)

#random decimal numbers
e=np.random.rand(4,2)
print(e)
f=np.random.random_sample(a.shape)
print(f)

#random integer values
g=np.random.randint(4,7,size=(3,3)) #4 to 7
print(g)

h=np.identity(5)
print(h)

arr=np.array([1,2,3])
r1=np.repeat(arr,3,axis=0)
print(r1)