import numpy as np
alpha = (1/2)*(4.523*10**10)**(-1/2)
y = np.random.normal(0,alpha,10000)
E_list = []
for x in y:
    e = (6.63*10**-34)*(10.483*10**6)*((-1/(2*9.046*10*10))*(-2*4.523*(10**10)+4*((4.523*10**10)**2)*x**2)+(1/2)*(9.046*10**10)*x**2)
    E_list.append(e)
E = sum(E_list)
E_ɸ = E/10000
print(E_ɸ)