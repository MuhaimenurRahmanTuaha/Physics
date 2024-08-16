# module import
import math
import matplotlib.pyplot as plt

# input
h = 0.005
k = 0.005

# row column calculation
r = int((0.5/k)+2)
c = int((1/h)+2)

# making an empty 2d list where the value of u,t,x will store
u = []
for i in range(r):
    l = []
    for j in range(c):
        l.append(0)
    u.append(l)

# adding the value of t and x in the table
for i in range(r):
    if i == r-1:
        u[i][0] = "t/x"
    else:
        u[i][0] = round((0.5 - i*k),3)
for i in range(c-1):
    u[r-1][i+1] = round((0 + i*h),3)    

# finding calculation of u at different t and x
for i in range(c-3):
    sin_degree = round(math.sin(math.radians(180*u[r-1][i+2])),4)
    u[r-2][i+2] = sin_degree
for j in range(c-3):
    u[r-3][j+2] = round(((u[(r-3)+1][(j+2)-1]+u[(r-3)+1][(j+2)+1])/2),4)
for i in range(r-3):
    for j in range(c-3):
        u[(r-1)-3-i][j+2] = round((u[(r-1)-3-i+1][j+2-1]+u[(r-1)-3-i+1][j+2+1]-u[(r-1)-3-i+2][j+2]),4)
for i in range(r):
    for j in range(c):
        print(format(u[i][j],"<10"), end=" ")
    print()

# x t and u data split for graph plot
x_value = []  
for j in range(1,c):
    x = u[r-1][j]
    x_value.append(x)
u_value_at_certain_t = []
for i in range(r-1):
    a = []
    for j in range(1,c):
        a.append(u[i][j])
    u_value_at_certain_t.append(a)

t_value = []
for i in range(r-1):
    t = u[i][0]
    t_value.append(t)

u_value_at_certain_x = []
for j in range(1,c):
    b = []
    for i in range(r-1):
        b.append(u[i][j])
    u_value_at_certain_x.append(b)

# graph plot
plt.subplot(1,2,1)
for i in range(len(u_value_at_certain_t)):
    plt.plot(x_value,u_value_at_certain_t[i])
plt.xlabel("value of x")
plt.ylabel("value of u")
plt.title("x vs u graph at certain t")
plt.legend()    

plt.subplot(1,2,2)
for i in range(len(u_value_at_certain_x)):
    plt.plot(t_value,u_value_at_certain_x[i])
plt.xlabel("value of t")
plt.ylabel("value of u")
plt.title("t vs u graph at certain x")
plt.legend()    
plt.show()
