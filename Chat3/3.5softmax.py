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


def softmax1(x):
    exp_a = np.exp(x)
    sum_exp_a = np.sum(exp_a)
    y = exp_a/sum_exp_a

    return y


z=np.array([1000,1010,990])
softmax1(z)
print ('softmax1(z)',softmax1(z))

c =np.max(z)
print ('c:',c)
print ('z-c:',z-c)

softmax1(z-c)
print ('softmax(z-c)',softmax1(z-c))


def softmax(a):
    c =np.max(a)
    exp_a = np.exp(c-a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a/sum_exp_a

    return y



a = np.array([1.6,3.8,3.9,2.6,0.69])
softmax(a)
print('softmax(a)',softmax(a))



