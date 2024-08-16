from vpython import *
from time import *
import math

WallThickness=0.1
RoomLength=12
Roomwidth=12
RoomHeight=4
floor= box(pos=vector(0,-RoomHeight/2,0),color = color.white,size=vector(RoomLength,WallThickness,Roomwidth))
# celling = box(pos=vector(0,RoomHeight/2,0),color = color.white,size=vector(RoomLength,WallThickness,Roomwidth))
leftwall=box(pos=vector(-RoomLength/2,0,0),color = color.white,size=vector(WallThickness,RoomHeight,Roomwidth))
rightwall=box(pos=vector(RoomLength/2,0,0),color = color.white,size=vector(WallThickness,RoomHeight,Roomwidth))
backwall=box(pos=vector(0,0,-Roomwidth/2),color = color.white,size=vector(RoomLength,RoomHeight,WallThickness))
table_surface=box(pos=vector(0,-.001,0),size=vector(7,0.005,7),color = color.yellow)
table_leg_front_left=box(pos=vector(-3.5+0.02/2,-2/2,3.5-0.02/2),size=vector(0.02,2,0.02),color = color.yellow)
table_leg_front_right=box(pos=vector(3.5-0.02/2,-2/2,3.5-0.02/2),size=vector(0.02,2,0.02),color = color.yellow)
table_leg_back_left=box(pos=vector(-3.5+0.02/2,-2/2,-3.5+0.02/2),size=vector(0.02,2,0.02),color = color.yellow)
table_leg_front_left=box(pos=vector(3.5-0.02/2,-2/2,-3.5+0.02/2),size=vector(0.02,2,0.02),color = color.yellow)
hole=cylinder(pos=vector(0,-.005,0),axis=vector(0,0.01,0), radius=0.075,color=color.black)

#input part (constant)
m1 = 6
m2 = 4
g = 9.8
L = 45
l = 3
#initial condition
t0 = 0
r0 = 2.5
v0 = 0
tetha0 =  15
tetha0 = tetha0*math.pi/180
#input value
h = 0.001

mm1=sphere(pos=r0*vector(cos(tetha0),0,sin(tetha0)),radius=0.1,color=color.green, make_trail=True)

s=((-1)*abs(l-r0))
mm2=sphere(pos=vector(0,s,0), radius=0.1,color=color.green)
string1=cylinder(pos=vector(0,0,0), axis=mm1.pos,radius=0.01,color=color.red)
string2=cylinder(pos=vector(0,0,0),axis=mm2.pos, radius=0.01,color=color.red)

#euler method
while True:
    rate(500)
    r = r0 + h*v0
    v = v0 + h*(((L**2)/(m1*(m1+m2)*(r**3)))-m2*g/(m1+m2))
    s = (-1)*abs(l-r)
    tetha = tetha0 + h*(L/(m1*(r**2)))
    tethadot = L/(m1*(r**2))
    mm1.pos=r*vector(cos(tetha),0,sin(tetha))
    mm2.pos=vector(0,s,0)
    string1.axis=mm1.pos
    string2.axis=mm2.pos
    r0 = r
    v0 = v
    tetha0 = tetha
