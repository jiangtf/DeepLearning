# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread


def sigmoid(x):
    return 1/(1 + np.exp(-x))

def indentify_function(x):
    return x



def init_network():
    network ={}
    network['W1'] = np.array([[0.2,0.5,0.3],[0.6,0.5,0.9]])
    network['b1'] = np.array([0.1,0.5,0.6])
    network['W2'] = np.array([ [0.2,0.5] ,[0.6,0.5] ,[0.7,0.9] ])
    network['b2'] = np.array([0.1,0.6])
    network['W3'] =  np.array([ [0.2,0.5] ,[0.6,0.5]  ])
    network['b3'] = np.array([0.43,0.66])
    print ('network:',network)
    print('network[W3]:', network['W3'])
    return network


def forward(network,x):
    W1,W2,W3 = network['W1'],network['W2'],network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x,W1) +b1
    z1 = sigmoid(a1)
    a2 = np.dot(a1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(a2, W3) + b3
    y = indentify_function(a3)


    return y


network = init_network()
x = np.array([3.69,2.58])
y = forward(network,x)

print('y',y)






