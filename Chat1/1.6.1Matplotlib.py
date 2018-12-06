# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt



x=np.arange(0,6,0.1)
print ('x:',x)
y=np.sin(x)
print ('y:',y)


plt.plot(x,y)
plt.show()