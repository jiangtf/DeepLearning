# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread


def relu(x):
    return np.maximum(0,x)


x=np.arange(-5.0,5.0,0.1)
print('x',x)
y=relu(x)
print('y',y)
plt.plot(x,y)
plt.show()

