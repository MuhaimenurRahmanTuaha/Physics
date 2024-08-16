# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 22:18:01 2022

@author: tashin
"""

import numpy as np
import math
import matplotlib.pyplot as plt

def calc1(x, y):
    sum = 0.5 * (x + y)
    return sum

def calc2(x, y, z):
    sum = x + y - z
    return sum

h, k = 0.125, 0.125
u = np.zeros((6,10))

for i in range(8):
    u[5][i+2] = round(u[5][i+1] +  h, 3)  # set value's of x
    
for i in range(8):
    u[4][i+2] = np.around(math.sin(math.pi * u[5][i+2]), 3)
    
for i in range (1):
    for j in range(7):
        u[3-i][j+2] = round(calc1(u[4-i][j+1], u[4-i][j+3]), 3) # iterate values of u
        u[3-i][0] = u[4-i][0] + k  # set value's of time
        
for i in range (3):
    for j in range(7):
        u[2-i][j+2] = round(calc2(u[3-i][j+1], u[3-i][j+3], u[4-i][j+2]), 3) # iterate values of u
        u[2-i][0] = u[3-i][0] + k  # set value's of time
        
        
plt.plot(u[5][1:], u[4][1:])
plt.plot(u[5][1:], u[3][1:])
plt.plot(u[5][1:], u[2][1:])
plt.plot(u[5][1:], u[1][1:])
plt.plot(u[5][1:], u[0][1:])
plt.title("x vs U(x) graph at certain t")
plt.ylabel('U(x)')
plt.xlabel('x')
plt.show()



plt.plot(u[:-1, 0], u[:-1, 2], '-')
plt.plot(u[:-1, 0], u[:-1, 3], 'bo--')
plt.plot(u[:-1, 0], u[:-1, 4], ':')
plt.plot(u[:-1, 0], u[:-1, 5], '--')
plt.title("t vs U(t) graph at certain x")
plt.ylabel('U(t)')
plt.xlabel('t')
plt.show()


for i in range(6):
    for j in range(10):
        if i == 5 and j ==0:
            print(format("t/x", "<10"), end=" ")
        else:
            print(format(u[i][j],"<10"), end=" ")
    print()