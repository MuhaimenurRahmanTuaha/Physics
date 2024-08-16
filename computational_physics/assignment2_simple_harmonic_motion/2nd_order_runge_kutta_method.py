import matplotlib.pyplot as plt
#user input
t0 = 0
x0 = 1
v0 = 0
t = float(input("final time (t) : "))
h = float(input("h : "))

#loop no calculation
n = round((t-t0)/h)

# differential equation solution
x = x0
v = v0
for i in range(n):
    k1 = h * v
    l1 = (-1) * h * x
    k2 = h * (v+l1)
    l2 = (-1) * h * (x+k1)
    x1 = x + (1/2) * (k1+k2)
    v1 = v + (1/2) * (l1+l2)
    x = x1
    v = v1
print(f"at {t} position is {x} and velocity is {v}")

#creating list for graph
time_list = [t0]
for i in range(1,200):
    t = t0 + h*i
    time_list.append(t)
    
position_list = [x0]
velocity_list = [v0]
    
# differential equation solution
x = x0
v = v0
for j in range(1,len(time_list)):
    k1 = h * v
    l1 = (-1) * h * x
    k2 = h * (v+l1)
    l2 = (-1) * h * (x+k1)
    x1 = x + (1/2) * (k1+k2)
    v1 = v + (1/2) * (l1+l2)
    position_list.append(x1)
    velocity_list.append(v1)
    x = x1
    v = v1

#graph ploting
plt.plot(time_list, position_list, label = "postion vs time" )
plt.plot(time_list, velocity_list, label = "velocity vs time")
plt.xlabel("time")
plt.legend()
plt.show()  