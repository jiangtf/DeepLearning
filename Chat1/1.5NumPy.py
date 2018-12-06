# -*- coding: utf-8 -*-

import numpy as np

x = np.array([1.0,2.0,3.0])
print ('x:',x)
print (type(x))
y = np.array([4.0,6.0,8.0])
print ('y:',y)
print ('x+y:',x+y)
print ('x-y:',x-y)
print ('x*y:',x*y)
print ('x/y:',x/y)
print ('x/2:',x/2)


a =np.array([[1,2],[3,4]])
print ('a:',a)
print ('a.shape:',a.shape)
print ('a.dtype:',a.dtype)
b =np.array([[3,5],[4,8]])
print ('b:',b)
print ('a+b:',a+b)
print ('a*b:',a*b)
print ('a*10:',a*10)


a =np.array([[1,2],[3,4]])
b =np.array([3,5])
print ('a*b:',a*b)

x =np.array([[1,2],[3,4],[5,6]])
print ('x:',x)
print ('x[0]:',x[0])
print ('x[0]:',x[0][0])

for row in x:
    print('row:', row)


x=x.flatten()
print ('x:',x)

print ('x[np.array([0,2,4])]:',x[np.array([0,2,4])])

print ('x>3:',x>3)
print ('x[x>3]:',x[x>3])















