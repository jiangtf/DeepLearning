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





