# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

a = np.array([1,2,3,4,5,6])
print ('a:',a)
print ('np.ndim(a):',np.ndim(a))
print ('a.ndim:',a.ndim)
print ('a.shape:',a.shape)
print ('a.shape:',a.shape[0])


b = np.array([[1,2],[3,4],[5,6]])
print ('b:',b)
print ('np.ndim(b):',np.ndim(b))
print ('b.ndim:',b.ndim)
print ('b.shape:',b.shape)
print ('b.shape[0]:',b.shape[0])
print ('b.shape[1]:',b.shape[1])


x = np.array([[1,2],[5,6]])
print ('x.shape:',x.shape)

y = np.array([[2,5],[2,2]])
print ('y.shape:',y.shape)
print ('np.dot(x,y):',np.dot(x,y))


x = np.array([[1,2,2],[3,5,6]])
print ('x.shape:',x.shape)

y = np.array([[2,5],[2,2],[8,9]])
print ('y.shape:',y.shape)
print ('np.dot(x,y):',np.dot(x,y))


x = np.array([[2,5],[2,2],[8,9]])
print ('x.shape:',x.shape)

y = np.array([2,5])
print ('y.shape:',y.shape)

print ('np.dot(x,y):',np.dot(x,y))












