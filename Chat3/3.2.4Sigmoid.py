# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread


def sigmoid(x):
    return 1/(1 + np.exp(-x))


x=np.arange(-5.0,5.0,0.1)
print('x',x)
y=sigmoid(x)
print('y',y)
plt.plot(x,y)
plt.show()

