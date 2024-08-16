# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 16:41:23 2022

@author: tashin
"""

import numpy as np
import math
import matplotlib.pyplot as plt

def calc(x, y):
    sum = 0.5 * (x + y)
    return sum

h, k = 0.2, 0.02
u = np.zeros((7,7))
# u[6][0] = "t/x"
for i in range(5):
    u[6][i+2] = round(u[6][i+1] +  h, 2)  # set value's of x

for i in range(5):
    u[5][i+2] = np.around(math.sin(math.pi * u[6][i+2]), 5)
    
for i in range (5):
    for j in range(4):
        u[4-i][j+2] = round(calc(u[5-i][j+1], u[5-i][j+3]), 4) # iterate values of u
        u[4-i][0] = u[5-i][0] + k  # set value's of time
        
plt.plot(u[6][1:], u[5][1:])
plt.plot(u[6][1:], u[4][1:])
plt.plot(u[6][1:], u[3][1:])
plt.plot(u[6][1:], u[2][1:])
plt.plot(u[6][1:], u[1][1:])
plt.plot(u[6][1:], u[0][1:])
plt.title("x vs U(x) graph at certain t")
plt.ylabel('U(x)')
plt.xlabel('x')
plt.show()

plt.plot(u[:-1, 0], u[:-1, 2], '-')
plt.plot(u[:-1, 0], u[:-1, 3], 'bo--')
plt.plot(u[:-1, 0], u[:-1, 4], '-')
plt.plot(u[:-1, 0], u[:-1, 5], '^k')
plt.title("t vs U(t) graph at certain x")
plt.ylabel('U(t)')
plt.xlabel('t')
plt.show()


for i in range(7):
    for j in range(7):
        if i == 6 and j ==0:
            print(format("t/x", "<10"), end=" ")
        else:
            print(format(u[i][j],"<10"), end=" ")
    print()