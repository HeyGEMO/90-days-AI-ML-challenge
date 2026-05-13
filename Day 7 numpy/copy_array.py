#becareful when copying arrays !!
import numpy as np
a=np.array([1,2,3])
b=a
b[0]=4
print(a)
print(b) #it changes value from both the array
#so to prevent that we use copy
c=a.copy()
c[0]=100
print(a)
print(c)
