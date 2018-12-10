# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

a = np.array([0.3,0.56,0.69])

exp_a =np.exp(a)
print('exp_a:',exp_a)


sum_exp_a = np.sum(exp_a)
print('sum_exp_a:',sum_exp_a)

y = exp_a /  sum_exp_a
print('y:',y)


def softmax(x):
    exp_a = np.exp(x)
    sum_exp_a = np.sum(exp_a)
    y = exp_a/sum_exp_a

    return y


z=np.array([1000,1010,990])
softmax(z)
print ('softmax(z)',softmax(z))

c =np.max(z)
print ('c:',c)
print ('z-c:',z-c)

softmax(z-c)
print ('softmax(z-c)',softmax(z-c))







