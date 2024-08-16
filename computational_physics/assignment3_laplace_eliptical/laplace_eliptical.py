u =[[1000,1000,1000,1000],[2000,'u_1,2','u_2,2',500],[2000,'u_1,1','u_2,1',0],[0,0,0,0]]
row = len(u)
columns = len(u[0])
print("Problem: Find out the value of u_1,2 , u_2,2 , u_1,1 , u_2,1 ")
for i in range(row):
    for j in range(columns):
        print(format(u[i][j],"<10"), end=" ")
    print()
print()
u[1][1]= (1/4)*(u[0][0]+u[0][2]+u[2][0]+0)
u[2][2]= (1/4)*(u[1][1]+u[1][3]+u[3][1]+u[3][3])
u[1][2]= (1/4)*(u[0][2]+u[1][1]+u[2][2]+u[1][3])
u[2][1]= (1/4)*(u[1][1]+u[2][0]+u[3][1]+u[2][2])
print("Using finite method")
for i in range(row):
    for j in range(columns):
        print(format(u[i][j],"<10"), end=" ")
    print()
print()
print("Jacobi's method")
while True:
    a = (1/4)*(u[0][1]+u[1][0]+u[2][1]+u[1][2])
    b = (1/4)*(u[0][2]+u[1][1]+u[2][2]+u[1][3])
    c = (1/4)*(u[1][1]+u[2][0]+u[3][1]+u[2][2])
    d = (1/4)*(u[1][2]+u[2][1]+u[3][2]+u[2][3])
    if u[1][1]-0.5<= a<= u[1][1]+0.5 and u[1][2]-0.5<= b<= u[1][2]+0.5 and u[2][1]-0.5<= c<= u[2][1]+0.5 and u[2][2]-0.5<= d<= u[2][2]+0.5:   
        break
    else:
        u[1][1] = a
        u[1][2] = b
        u[2][1] = c
        u[2][2] = d

for i in range(row):
    for j in range(columns):
        print(format(u[i][j],"<20"), end=" ")
    print()
print()
print("Gauss seidal method")
while True:
    a = (1/4)*(u[0][1]+u[1][0]+u[2][1]+u[1][2])
    b = (1/4)*(u[0][2]+a+u[2][2]+u[1][3])
    c = (1/4)*(a+u[2][0]+u[3][1]+u[2][2])
    d = (1/4)*(b+c+u[3][2]+u[2][3])
    if u[1][1]-0.5<= a<= u[1][1]+0.5 and u[1][2]-0.5<= b<= u[1][2]+0.5 and u[2][1]-0.5<= c<= u[2][1]+0.5 and u[2][2]-0.5<= d<= u[2][2]+0.5:   
        break
    else:
        u[1][1] = a
        u[1][2] = b
        u[2][1] = c
        u[2][2] = d

for i in range(row):
    for j in range(columns):
        print(format(u[i][j],"<20"), end=" ")
    print()


    
