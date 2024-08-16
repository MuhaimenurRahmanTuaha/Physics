# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np


# Jacobi's methode
c = 0.25 * (1000 + 1000 + 2000 + 0)
d = 0.25 * (1000 + 1000 + 0 + 0)
a = 0.25 * (1000 + 2000 + 0 + 0)
b = 0.25 * (1000 + 2000 + 0 + 0)

u1, u2, u3, u4 = [0], [0], [0], [0]
for i in range(9999):
    p = 0.25 * (2000 + b + c + 0)
    q = 0.25 * (a + 0 + d + 0)
    r = 0.25 * (1000 + a + 2000 + d)
    s = 0.25 * (1000 + b + c + 500)
    u1.append(p)
    u2.append(q)
    u3.append(r)
    u4.append(s)
    a, b, c, d = p, q, r, s
    if np.abs(u1[i]-u1[i-1]) < 0.001 and np.abs(u2[i]-u2[i-1]) < 0.001 and np.abs(u3[i]-u3[i-1]) < 0.001 and np.abs(u4[i]-u4[i-1]) < 0.001:
        break
    

sol_jac = {}
sol_jac['u11'] = u1
sol_jac['u21'] = u2
sol_jac['u12'] = u3
sol_jac['u22'] = u4
solJac = pd.DataFrame(sol_jac)
print('Jacobi\'s methode:')
print(solJac, '\n')
print("NB: Iteration stopped when two corresponding values difference is less then 0.001")
print('\n\n')


#Gauss-Seidel's method
a, b, c, d = 0, 0, 0, 0
c = 0.25 * (1000 + 1000 + 2000 + 0)
d = 0.25 * (1000 + b + c + 500)
a = 0.25 * (2000 + b + d + 0)
b = 0.25 * (a + d + 0 + 0)

v1, v2, v3, v4 = [0], [0], [0], [0]
for i in range(9999):
    a = 0.25 * (2000 + b + c + 0)
    b = 0.25 * (a + 0 + d + 0)
    c = 0.25 * (1000 + a + 2000 + d)
    d = 0.25 * (1000 + b + c + 500)
    v1.append(a)
    v2.append(b)
    v3.append(c)
    v4.append(d)
    if np.abs(v1[i] - v1[i-1]) < 0.001 and np.abs(v2[i] - v2[i-1]) < 0.001 and np.abs(v3[i] - v3[i-1]) < 0.001 and np.abs(v4[i] - v4[i-1]) < 0.001:
        break


sol_gauss = {}
sol_gauss['v11'] = v1
sol_gauss['v21'] = v2
sol_gauss['v12'] = v3
sol_gauss['v22'] = v4
solGauss = pd.DataFrame(sol_gauss)
print("Gauss-Seidel's method:")
print(solGauss, '\n')
print("NB: Iteration stopped when two corresponding values difference is less then 0.001")
