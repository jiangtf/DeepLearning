# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

def setp_fuction1(x):
    if x > 0:
        return 1
    else:
        return 0



def setp_fuction2(x):
    y = x > 0
    print ('y',y)
    return y.astype(np.int)


print ( 'setp_fuction2(np.array([-1,-2,-3,1,2,3]):',setp_fuction2(np.array([-1,-2,-3,1,2,3])))


def setp_fuction(x):
    return np.array(x>0,dtype=np.int)


x=np.arange(-5.0,5.0,0.1)
y=setp_fuction(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()