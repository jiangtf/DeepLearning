# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread



x = np.array([1,0.5])
w1 = np.array([[0.2,0.5,0.3],[0.6,0.5,0.9]])
b1 = np.array([0.1,0.5,0.6])

print ('x.shape:',x.shape)
print ('w1.shape:',w1.shape)
print ('b1.shape:',b1.shape)


a1 = np.dot(x,w1) + b1
print ('a1:',a1)

def sigmoid(x):
    return 1/(1 + np.exp(-x))

z1=sigmoid(a1)
print ('z1:',z1)



w2 = np.array([ [0.2,0.5] ,[0.6,0.5] ,[0.7,0.9] ])
b2 = np.array([0.1,0.6])

print ('z1.shape:',z1.shape)
print ('w2.shape:',w2.shape)
print ('b2.shape:',b2.shape)

a2 = np.dot(z1,w2) + b2
print ('a2.shape:',a2.shape)

z2=sigmoid(a2)
print ('z2:',z2)

def indentify_function(x):
    return x

w3 =  np.array([ [0.2,0.5] ,[0.6,0.5]  ])
b3 = np.array([0.43,0.6])

a2 = np.dot(z2,w3) + b3
print ('a2:',a2)

y= indentify_function(a2)
print ('y:',y)









