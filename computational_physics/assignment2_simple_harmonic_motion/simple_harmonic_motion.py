#library input
import matplotlib.pyplot as plt
import numpy as np
import math 
from fractions import Fraction

#method selection
print("Please a method:\n 1. 2nd order Runge Kutta method,\n 2. 4th order Runge Kutta method ,\n 3. postion comparison graph between 2nd and 4th order Runge Kutta method,\n 4. velocity comparison graph between 2nd and 4th order Runge Kutta method ,\n 5.postion and velocity value comparison between 2nd and 4th order Runge Kutta method,\n 6.position comparison graph between 2nd order 4th order Runge Kutta method and analytical value,\n 7. velocity comparison graph between 2nd order 4th order Runge Kutta method and analytical value")
method = input("Please type '1' or '2' or '3' or '4' or '5' or '6' or '7': ")

if method == "1":
    print("What do you want?")
    print("1. postion and velocity at a certain time,\n 2. graph of postion and velocity,\n 3. graph of postion and velocity and also value of position and velocity at a certain time,\n 4. comparison position vs time graph with analytical graph,\n 5. comparison velocity vs time graph with analytical graph,\n 6. position vs time, velocity vs time and analytical graph for position and velocity with respect to time ")
    method1 = input("Please select '1' or '2' or '3' or '4' or '5' or '6' : ")
    if method1 == "1":
        #user input
        t0 = float(input("initial time (t0) : "))
        x0 = float(input("initial position (x0) : "))
        v0 = float(input("initial velocity (v0) : "))
        t = float(input("final value of t : "))
        k = float(input("spring constant (k) : "))
        m = float(input("mass of spring (m) : "))
        h = float(input("value of h : "))
        
        #constant calculation
        const = k/m
        
        #loop no calculation
        n = round((t-t0)/h)
        
        # differential equation solution
        x = x0
        v = v0
        for i in range(n):
            k1 = h * v
            l1 = (-1) * h * const * x
            k2 = h * (v+l1)
            l2 = (-1) * h * const * (x+k1)
            x1 = x + (1/2) * (k1+k2)
            v1 = v + (1/2) * (l1+l2)
            x = x1
            v = v1
        print(f"at {t} position is {x} and velocity is {v}")
    elif method1 == "2":
        #user input
        t0 = float(input("initial time (t0) : "))
        x0 = float(input("initial position (x0) : "))
        v0 = float(input("initial velocity (v0) : "))
        k = float(input("spring constant (k) : "))
        m = float(input("mass of spring (m) : "))
        h = float(input("value of h : "))
        
        #constant calculation
        const = k/m
        
        #creating list for graph
        time_list = [t0]
        for i in range(1,400):
            t = t0 + h*i
            time_list.append(t)
        
        position_list = [x0]
        velocity_list = [v0]

        # differential equation solution
        x = x0
        v = v0
        for j in range(1,len(time_list)):
            k1 = h * v
            l1 = (-1) * h * const * x
            k2 = h * (v+l1)
            l2 = (-1) * h * const * (x+k1)
            x1 = x + (1/2) * (k1+k2)
            v1 = v + (1/2) * (l1+l2)
            position_list.append(x1)
            velocity_list.append(v1)
            x = x1
            v = v1
        
        #graph ploting
        plt.plot(time_list, position_list, label = "postion vs time graph" )
        plt.plot(time_list, velocity_list, label = "velocity vs time graph")
        plt.xlabel("time")
        plt.legend()
        plt.show()
        
    elif method1 == "3":
    
        #user input
        t0 = float(input("initial time (t0) : "))
        x0 = float(input("initial position (x0) : "))
        v0 = float(input("initial velocity (v0) : "))
        t = float(input("final value of t : "))
        k = float(input("spring constant (k) : "))
        m = float(input("mass of spring (m) : "))
        h = float(input("value of h : "))
        
        #constant calculation
        const = k/m
        
        #loop no calculation
        n = round((t-t0)/h)
        
        # differential equation solution
        x = x0
        v = v0
        for i in range(n):
            k1 = h * v
            l1 = (-1) * h * const * x
            k2 = h * (v+l1)
            l2 = (-1) * h * const * (x+k1)
            x1 = x + (1/2) * (k1+k2)
            v1 = v + (1/2) * (l1+l2)
            x = x1
            v = v1
        print(f"at {t} position is {x} and velocity is {v}")

        #creating list for graph
        time_list = [t0]
        for i in range(1,400):
            t = t0 + h*i
            time_list.append(t)
        
        position_list = [x0]
        velocity_list = [v0]

        # differential equation solution
        x = x0
        v = v0
        for j in range(1,len(time_list)):
            k1 = h * v
            l1 = (-1) * h * const * x
            k2 = h * (v+l1)
            l2 = (-1) * h * const * (x+k1)
            x1 = x + (1/2) * (k1+k2)
            v1 = v + (1/2) * (l1+l2)
            position_list.append(x1)
            velocity_list.append(v1)
            x = x1
            v = v1
        
        #graph ploting
        plt.plot(time_list, position_list, label = "postion vs time graph" )
        plt.plot(time_list, velocity_list, label = "velocity vs time graph")
        plt.xlabel("time")
        plt.legend()
        plt.show()  
    
    elif method1 == "4":

        #user input
        t0 = float(input("initial time (t0) : "))
        x0 = float(input("initial position (x0) : "))
        v0 = float(input("initial velocity (v0) : "))
        k = float(input("spring constant (k) : "))
        m = float(input("mass of spring (m) : "))
        h = float(input("value of h : "))
        
        #constant calculation
        const = k/m
        
        #creating list for graph
        time_list = [t0]
        for i in range(1,400):
            t = t0 + h*i
            time_list.append(t)
        
        position_list = [x0]
        velocity_list = [v0]

        # differential equation solution
        x = x0
        v = v0
        for j in range(1,len(time_list)):
            k1 = h * v
            l1 = (-1) * h * const * x
            k2 = h * (v+l1)
            l2 = (-1) * h * const * (x+k1)
            x1 = x + (1/2) * (k1+k2)
            v1 = v + (1/2) * (l1+l2)
            position_list.append(x1)
            velocity_list.append(v1)
            x = x1
            v = v1
        
        #analytical data
        analytical_position_list = []
        if t0 == 0 and v0 == 0:
            for k in range(len(time_list)):
                analytical_data = x0 * math.cos(math.sqrt(const)*time_list[k])
                analytical_position_list.append(analytical_data)
        else:
            delta = math.atan((-1) * v0 / (x0 * math.sqrt(const))) - math.sqrt(const) * t0
            amplitude = x0 / (math.cos(math.sqrt(const) * t0 + delta))
            for k in range(len(time_list)):
                analytical_data = amplitude * math.cos(math.sqrt(const)*time_list[k] + delta)
                analytical_position_list.append(analytical_data)
        
        #graph ploting
        plt.plot(time_list, position_list, label = "postion vs time graph" )
        plt.plot(time_list, analytical_position_list, '-.' , label = "analytical data")
        plt.xlabel("time")
        plt.legend()
        plt.show()        

    elif method1 == "5":

        #user input
        t0 = float(input("initial time (t0) : "))
        x0 = float(input("initial position (x0) : "))
        v0 = float(input("initial velocity (v0) : "))
        k = float(input("spring constant (k) : "))
        m = float(input("mass of spring (m) : "))
        h = float(input("value of h : "))
        
        #constant calculation
        const = k/m
        
        #creating list for graph
        time_list = [t0]
        for i in range(1,400):
            t = t0 + h*i
            time_list.append(t)
        
        position_list = [x0]
        velocity_list = [v0]

        # differential equation solution
        x = x0
        v = v0
        for j in range(1,len(time_list)):
            k1 = h * v
            l1 = (-1) * h * const * x
            k2 = h * (v+l1)
            l2 = (-1) * h * const * (x+k1)
            x1 = x + (1/2) * (k1+k2)
            v1 = v + (1/2) * (l1+l2)
            position_list.append(x1)
            velocity_list.append(v1)
            x = x1
            v = v1
        
        #analytical data
        analytical_velocity_list = []
        if t0 == 0 and v0 == 0:
            for k in range(len(time_list)):
                analytical_data = (-1) * math.sqrt(const) * x0 * math.sin(math.sqrt(const)*time_list[k])
                analytical_velocity_list.append(analytical_data)
        else:
            delta = math.atan((-1) * v0 / (x0 * math.sqrt(const))) - math.sqrt(const) * t0
            amplitude = x0 / (math.cos(math.sqrt(const) * t0 + delta))
            for k in range(len(time_list)):
                analytical_data = (-1) * math.sqrt(const) * amplitude * math.sin(math.sqrt(const)*time_list[k] + delta)
                analytical_velocity_list.append(analytical_data)
        
        #graph ploting
        plt.plot(time_list, velocity_list, label = "velocity vs time graph" )
        plt.plot(time_list, analytical_velocity_list, '-.' , label = "analytical data")
        plt.xlabel("time")
        plt.legend()
        plt.show()        

    elif method1 == "6":

        #user input
        t0 = float(input("initial time (t0) : "))
        x0 = float(input("initial position (x0) : "))
        v0 = float(input("initial velocity (v0) : "))
        k = float(input("spring constant (k) : "))
        m = float(input("mass of spring (m) : "))
        h = float(input("value of h : "))
        
        #constant calculation
        const = k/m
        
        #creating list for graph
        time_list = [t0]
        for i in range(1,400):
            t = t0 + h*i
            time_list.append(t)
        
        position_list = [x0]
        velocity_list = [v0]

        # differential equation solution
        x = x0
        v = v0
        for j in range(1,len(time_list)):
            k1 = h * v
            l1 = (-1) * h * const * x
            k2 = h * (v+l1)
            l2 = (-1) * h * const * (x+k1)
            x1 = x + (1/2) * (k1+k2)
            v1 = v + (1/2) * (l1+l2)
            position_list.append(x1)
            velocity_list.append(v1)
            x = x1
            v = v1
        
        #analytical position data
        analytical_position_list = []
        if t0 == 0 and v0 == 0:
            for k in range(len(time_list)):
                analytical_data = x0 * math.cos(math.sqrt(const)*time_list[k])
                analytical_position_list.append(analytical_data)
        else:
            delta = math.atan((-1) * v0 / (x0 * math.sqrt(const))) - math.sqrt(const) * t0
            amplitude = x0 / (math.cos(math.sqrt(const) * t0 + delta))
            for k in range(len(time_list)):
                analytical_data = amplitude * math.cos(math.sqrt(const)*time_list[k] + delta)
                analytical_position_list.append(analytical_data)

        #analytical velocity data
        analytical_velocity_list = []
        if t0 == 0 and v0 == 0:
            for k in range(len(time_list)):
                analytical_data = (-1) * math.sqrt(const) * x0 * math.sin(math.sqrt(const)*time_list[k])
                analytical_velocity_list.append(analytical_data)
        else:
            delta = math.atan((-1) * v0 / (x0 * math.sqrt(const))) - math.sqrt(const) * t0
            amplitude = x0 / (math.cos(math.sqrt(const) * t0 + delta))
            for k in range(len(time_list)):
                analytical_data = (-1) * math.sqrt(const) * amplitude * math.sin(math.sqrt(const)*time_list[k] + delta)
                analytical_velocity_list.append(analytical_data)
        
        #graph ploting
        plt.plot(time_list, position_list, label = "postion vs time graph" )
        plt.plot(time_list, analytical_position_list, '-.' , label = "analytical graph for position")
        plt.plot(time_list, velocity_list, label = "velocity vs time graph")
        plt.plot(time_list, analytical_velocity_list, '-.' , label = "analytical  graph for velocity")
        plt.xlabel("time")
        plt.legend()
        plt.show()        

elif method == "2":
    print("What do you want?")
    print("1. postion and velocity at a certain time,\n 2. graph of postion and velocity,\n 3. graph of postion and velocity and also value of position and velocity at a certain time,\n 4. comparison position vs time graph with analytical graph,\n 5. comparison velocity vs time graph with analytical graph,\n 6. position vs time, velocity vs time and analytical graph for position and velocity with respect to time ")
    method1 = input("Please select '1' or '2' or '3' or '4' or '5' or '6' : ")
    if method1 == "1":
        #user input
        t0 = float(input("initial time (t0) : "))
        x0 = float(input("initial position (x0) : "))
        v0 = float(input("initial velocity (v0) : "))
        t = float(input("final value of t : "))
        k = float(input("spring constant (k) : "))
        m = float(input("mass of spring (m) : "))
        h = float(input("value of h : "))
        
        #constant calculation
        const = k/m
        
        #loop no calculation
        n = round((t-t0)/h)
        
        # differential equation solution
        x = x0
        v = v0
        for i in range(n):
            k1 = h * v
            l1 = (-1) * h * const * x
            k2 = h * (v + l1 / 2)
            l2 = (-1) * h * const * (x+ k1 / 2)
            k3 = h * (v + l2 / 2)
            l3 = (-1) * h * const * (x+ k2 / 2)
            k4 = h * (v + l3)
            l4 = (-1) * h * const * (x+ k3)
            x1 = x + (1/6) * (k1+2*k2+2*k3+k4)
            v1 = v + (1/6) * (l1+2*l2+2*l3+l4)
            x = x1
            v = v1
        print(f"at {t} position is {x} and velocity is {v}")       
    
    elif method1 == "2":
        #user input
        t0 = float(input("initial time (t0) : "))
        x0 = float(input("initial position (x0) : "))
        v0 = float(input("initial velocity (v0) : "))
        k = float(input("spring constant (k) : "))
        m = float(input("mass of spring (m) : "))
        h = float(input("value of h : "))
        
        #constant calculation
        const = k/m
        
        #creating list for graph
        time_list = [t0]
        for i in range(1,400):
            t = t0 + h*i
            time_list.append(t)
        
        position_list = [x0]
        velocity_list = [v0]

        # differential equation solution
        x = x0
        v = v0
        for j in range(1,len(time_list)):
            k1 = h * v
            l1 = (-1) * h * const * x
            k2 = h * (v + l1 / 2)
            l2 = (-1) * h * const * (x+ k1 / 2)
            k3 = h * (v + l2 / 2)
            l3 = (-1) * h * const * (x+ k2 / 2)
            k4 = h * (v + l3)
            l4 = (-1) * h * const * (x+ k3)
            x1 = x + (1/6) * (k1+2*k2+2*k3+k4)
            v1 = v + (1/6) * (l1+2*l2+2*l3+l4)
            position_list.append(x1)
            velocity_list.append(v1)
            x = x1
            v = v1
        
        #graph ploting
        plt.plot(time_list, position_list, label = "postion vs time graph" )
        plt.plot(time_list, velocity_list, label = "velocity vs time graph")
        plt.xlabel("time")
        plt.legend()
        plt.show()

    elif method1 == "3":
    
        #user input
        t0 = float(input("initial time (t0) : "))
        x0 = float(input("initial position (x0) : "))
        v0 = float(input("initial velocity (v0) : "))
        t = float(input("final value of t : "))
        k = float(input("spring constant (k) : "))
        m = float(input("mass of spring (m) : "))
        h = float(input("value of h : "))
        
        #constant calculation
        const = k/m
        
        #loop no calculation
        n = round((t-t0)/h)
        
        # differential equation solution
        x = x0
        v = v0
        for i in range(n):
            k1 = h * v
            l1 = (-1) * h * const * x
            k2 = h * (v + l1 / 2)
            l2 = (-1) * h * const * (x+ k1 / 2)
            k3 = h * (v + l2 / 2)
            l3 = (-1) * h * const * (x+ k2 / 2)
            k4 = h * (v + l3)
            l4 = (-1) * h * const * (x+ k3)
            x1 = x + (1/6) * (k1+2*k2+2*k3+k4)
            v1 = v + (1/6) * (l1+2*l2+2*l3+l4)
            x = x1
            v = v1
        print(f"at {t} position is {x} and velocity is {v}")

        #creating list for graph
        time_list = [t0]
        for i in range(1,400):
            t = t0 + h*i
            time_list.append(t)
        
        position_list = [x0]
        velocity_list = [v0]

        # differential equation solution
        x = x0
        v = v0
        for j in range(1,len(time_list)):
            k1 = h * v
            l1 = (-1) * h * const * x
            k2 = h * (v + l1 / 2)
            l2 = (-1) * h * const * (x+ k1 / 2)
            k3 = h * (v + l2 / 2)
            l3 = (-1) * h * const * (x+ k2 / 2)
            k4 = h * (v + l3)
            l4 = (-1) * h * const * (x+ k3)
            x1 = x + (1/6) * (k1+2*k2+2*k3+k4)
            v1 = v + (1/6) * (l1+2*l2+2*l3+l4)
            position_list.append(x1)
            velocity_list.append(v1)
            x = x1
            v = v1
        
        #graph ploting
        plt.plot(time_list, position_list, label = "postion vs time graph" )
        plt.plot(time_list, velocity_list, label = "velocity vs time graph")
        plt.xlabel("time")
        plt.legend()
        plt.show()  
    
    elif method1 == "4":

        #user input
        t0 = float(input("initial time (t0) : "))
        x0 = float(input("initial position (x0) : "))
        v0 = float(input("initial velocity (v0) : "))
        k = float(input("spring constant (k) : "))
        m = float(input("mass of spring (m) : "))
        h = float(input("value of h : "))
        
        #constant calculation
        const = k/m
        
        #creating list for graph
        time_list = [t0]
        for i in range(1,400):
            t = t0 + h*i
            time_list.append(t)
        
        position_list = [x0]
        velocity_list = [v0]

        # differential equation solution
        x = x0
        v = v0
        for j in range(1,len(time_list)):
            k1 = h * v
            l1 = (-1) * h * const * x
            k2 = h * (v + l1 / 2)
            l2 = (-1) * h * const * (x+ k1 / 2)
            k3 = h * (v + l2 / 2)
            l3 = (-1) * h * const * (x+ k2 / 2)
            k4 = h * (v + l3)
            l4 = (-1) * h * const * (x+ k3)
            x1 = x + (1/6) * (k1+2*k2+2*k3+k4)
            v1 = v + (1/6) * (l1+2*l2+2*l3+l4)
            position_list.append(x1)
            velocity_list.append(v1)
            x = x1
            v = v1
        
        #analytical data
        analytical_position_list = []
        if t0 == 0 and v0 == 0:
            for k in range(len(time_list)):
                analytical_data = x0 * math.cos(math.sqrt(const)*time_list[k])
                analytical_position_list.append(analytical_data)
        else:
            delta = math.atan((-1) * v0 / (x0 * math.sqrt(const))) - math.sqrt(const) * t0
            amplitude = x0 / (math.cos(math.sqrt(const) * t0 + delta))
            for k in range(len(time_list)):
                analytical_data = amplitude * math.cos(math.sqrt(const)*time_list[k] + delta)
                analytical_position_list.append(analytical_data)
        
        #graph ploting
        plt.plot(time_list, position_list, label = "postion vs time graph" )
        plt.plot(time_list, analytical_position_list, '-.' , label = "analytical data")
        plt.xlabel("time")
        plt.legend()
        plt.show()        

    elif method1 == "5":

        #user input
        t0 = float(input("initial time (t0) : "))
        x0 = float(input("initial position (x0) : "))
        v0 = float(input("initial velocity (v0) : "))
        k = float(input("spring constant (k) : "))
        m = float(input("mass of spring (m) : "))
        h = float(input("value of h : "))
        
        #constant calculation
        const = k/m
        
        #creating list for graph
        time_list = [t0]
        for i in range(1,400):
            t = t0 + h*i
            time_list.append(t)
        
        position_list = [x0]
        velocity_list = [v0]

        # differential equation solution
        x = x0
        v = v0
        for j in range(1,len(time_list)):
            k1 = h * v
            l1 = (-1) * h * const * x
            k2 = h * (v + l1 / 2)
            l2 = (-1) * h * const * (x+ k1 / 2)
            k3 = h * (v + l2 / 2)
            l3 = (-1) * h * const * (x+ k2 / 2)
            k4 = h * (v + l3)
            l4 = (-1) * h * const * (x+ k3)
            x1 = x + (1/6) * (k1+2*k2+2*k3+k4)
            v1 = v + (1/6) * (l1+2*l2+2*l3+l4)
            position_list.append(x1)
            velocity_list.append(v1)
            x = x1
            v = v1
        
        #analytical data
        analytical_velocity_list = []
        if t0 == 0 and v0 == 0:
            for k in range(len(time_list)):
                analytical_data = (-1) * math.sqrt(const) * x0 * math.sin(math.sqrt(const)*time_list[k])
                analytical_velocity_list.append(analytical_data)
        else:
            delta = math.atan((-1) * v0 / (x0 * math.sqrt(const))) - math.sqrt(const) * t0
            amplitude = x0 / (math.cos(math.sqrt(const) * t0 + delta))
            for k in range(len(time_list)):
                analytical_data = (-1) * math.sqrt(const) * amplitude * math.sin(math.sqrt(const)*time_list[k] + delta)
                analytical_velocity_list.append(analytical_data)
        
        #graph ploting
        plt.plot(time_list, velocity_list, label = "velocity vs time graph" )
        plt.plot(time_list, analytical_velocity_list, '-.' , label = "analytical data")
        plt.xlabel("time")
        plt.legend()
        plt.show()        

    elif method1 == "6":

        #user input
        t0 = float(input("initial time (t0) : "))
        x0 = float(input("initial position (x0) : "))
        v0 = float(input("initial velocity (v0) : "))
        k = float(input("spring constant (k) : "))
        m = float(input("mass of spring (m) : "))
        h = float(input("value of h : "))
        
        #constant calculation
        const = k/m
        
        #creating list for graph
        time_list = [t0]
        for i in range(1,400):
            t = t0 + h*i
            time_list.append(t)
        
        position_list = [x0]
        velocity_list = [v0]

        # differential equation solution
        x = x0
        v = v0
        for j in range(1,len(time_list)):
            k1 = h * v
            l1 = (-1) * h * const * x
            k2 = h * (v + l1 / 2)
            l2 = (-1) * h * const * (x+ k1 / 2)
            k3 = h * (v + l2 / 2)
            l3 = (-1) * h * const * (x+ k2 / 2)
            k4 = h * (v + l3)
            l4 = (-1) * h * const * (x+ k3)
            x1 = x + (1/6) * (k1+2*k2+2*k3+k4)
            v1 = v + (1/6) * (l1+2*l2+2*l3+l4)
            position_list.append(x1)
            velocity_list.append(v1)
            x = x1
            v = v1
        
        #analytical position data
        analytical_position_list = []
        if t0 == 0 and v0 == 0:
            for k in range(len(time_list)):
                analytical_data = x0 * math.cos(math.sqrt(const)*time_list[k])
                analytical_position_list.append(analytical_data)
        else:
            delta = math.atan((-1) * v0 / (x0 * math.sqrt(const))) - math.sqrt(const) * t0
            amplitude = x0 / (math.cos(math.sqrt(const) * t0 + delta))
            for k in range(len(time_list)):
                analytical_data = amplitude * math.cos(math.sqrt(const)*time_list[k] + delta)
                analytical_position_list.append(analytical_data)

        #analytical velocity data
        analytical_velocity_list = []
        if t0 == 0 and v0 == 0:
            for k in range(len(time_list)):
                analytical_data = (-1) * math.sqrt(const) * x0 * math.sin(math.sqrt(const)*time_list[k])
                analytical_velocity_list.append(analytical_data)
        else:
            delta = math.atan((-1) * v0 / (x0 * math.sqrt(const))) - math.sqrt(const) * t0
            amplitude = amplitude / (math.cos(math.sqrt(const) * t0 + delta))
            for k in range(len(time_list)):
                analytical_data = (-1) * math.sqrt(const) * amplitude * math.sin(math.sqrt(const)*time_list[k] + delta)
                analytical_velocity_list.append(analytical_data)
        
        #graph ploting
        plt.plot(time_list, position_list, label = "postion vs time graph" )
        plt.plot(time_list, analytical_position_list, '-.' , label = "analytical graph for position")
        plt.plot(time_list, velocity_list, label = "velocity vs time graph")
        plt.plot(time_list, analytical_velocity_list, '-.' , label = "analytical  graph for velocity")
        plt.xlabel("time")
        plt.legend()
        plt.show()        

elif method == "3":
    #user input
    t0 = float(input("initial time (t0) : "))
    x0 = float(input("initial position (x0) : "))
    v0 = float(input("initial velocity (v0) : "))
    k = float(input("spring constant (k) : "))
    m = float(input("mass of spring (m) : "))
    h = float(input("value of h : "))
        
    #constant calculation
    const = k/m
        
    #creating list for graph
    time_list = [t0]
    for i in range(1,400):
        t = t0 + h*i
        time_list.append(t)
        
    second_order_position_list = [x0]
    second_order_velocity_list = [v0]

    # differential equation solution
    x = x0
    v = v0
    for j in range(1,len(time_list)):
        k1 = h * v
        l1 = (-1) * h * const * x
        k2 = h * (v+l1)
        l2 = (-1) * h * const * (x+k1)
        x1 = x + (1/2) * (k1+k2)
        v1 = v + (1/2) * (l1+l2)
        second_order_position_list.append(x1)
        second_order_velocity_list.append(v1)
        x = x1
        v = v1
    forth_order_position_list = [x0]
    forth_order_velocity_list = [v0]

    # differential equation solution
    x = x0
    v = v0
    for j in range(1,len(time_list)):
        k1 = h * v
        l1 = (-1) * h * const * x
        k2 = h * (v + l1 / 2)
        l2 = (-1) * h * const * (x+ k1 / 2)
        k3 = h * (v + l2 / 2)
        l3 = (-1) * h * const * (x+ k2 / 2)
        k4 = h * (v + l3)
        l4 = (-1) * h * const * (x+ k3)
        x1 = x + (1/6) * (k1+2*k2+2*k3+k4)
        v1 = v + (1/6) * (l1+2*l2+2*l3+l4)
        forth_order_position_list.append(x1)
        forth_order_velocity_list.append(v1)
        x = x1
        v = v1
    
    #graph plot
    plt.plot(time_list, second_order_position_list, label = "2nd order Runge Kutta method")
    plt.plot(time_list, forth_order_position_list, '-.',  label = "4th order Runge Kutta method")
    plt.legend()
    plt.show()
    
elif method == "4":
    #user input
    t0 = float(input("initial time (t0) : "))
    x0 = float(input("initial position (x0) : "))
    v0 = float(input("initial velocity (v0) : "))
    k = float(input("spring constant (k) : "))
    m = float(input("mass of spring (m) : "))
    h = float(input("value of h : "))
        
    #constant calculation
    const = k/m
        
    #creating list for graph
    time_list = [t0]
    for i in range(1,400):
        t = t0 + h*i
        time_list.append(t)
        
    second_order_position_list = [x0]
    second_order_velocity_list = [v0]

    # differential equation solution
    x = x0
    v = v0
    for j in range(1,len(time_list)):
        k1 = h * v
        l1 = (-1) * h * const * x
        k2 = h * (v+l1)
        l2 = (-1) * h * const * (x+k1)
        x1 = x + (1/2) * (k1+k2)
        v1 = v + (1/2) * (l1+l2)
        second_order_position_list.append(x1)
        second_order_velocity_list.append(v1)
        x = x1
        v = v1
    forth_order_position_list = [x0]
    forth_order_velocity_list = [v0]

    # differential equation solution
    x = x0
    v = v0
    for j in range(1,len(time_list)):
        k1 = h * v
        l1 = (-1) * h * const * x
        k2 = h * (v + l1 / 2)
        l2 = (-1) * h * const * (x+ k1 / 2)
        k3 = h * (v + l2 / 2)
        l3 = (-1) * h * const * (x+ k2 / 2)
        k4 = h * (v + l3)
        l4 = (-1) * h * const * (x+ k3)
        x1 = x + (1/6) * (k1+2*k2+2*k3+k4)
        v1 = v + (1/6) * (l1+2*l2+2*l3+l4)
        forth_order_position_list.append(x1)
        forth_order_velocity_list.append(v1)
        x = x1
        v = v1
    
    #graph plot
    plt.plot(time_list, second_order_velocity_list,  label = "2nd order Runge Kutta method")
    plt.plot(time_list, forth_order_velocity_list, '-.', label = "4th order Runge Kutta method")
    plt.legend()
    plt.show()
    
elif method == "5":
    #user input
    t0 = float(input("initial time (t0) : "))
    x0 = float(input("initial position (x0) : "))
    v0 = float(input("initial velocity (v0) : "))
    k = float(input("spring constant (k) : "))
    m = float(input("mass of spring (m) : "))
    h = float(input("value of h : "))
        
    #constant calculation
    const = k/m
        
    #creating list for graph
    time_list = [t0]
    for i in range(1,400):
        t = t0 + h*i
        time_list.append(t)
        
    second_order_position_list = [x0]
    second_order_velocity_list = [v0]

    # differential equation solution
    x = x0
    v = v0
    for j in range(1,len(time_list)):
        k1 = h * v
        l1 = (-1) * h * const * x
        k2 = h * (v+l1)
        l2 = (-1) * h * const * (x+k1)
        x1 = x + (1/2) * (k1+k2)
        v1 = v + (1/2) * (l1+l2)
        second_order_position_list.append(x1)
        second_order_velocity_list.append(v1)
        x = x1
        v = v1
    forth_order_position_list = [x0]
    forth_order_velocity_list = [v0]

    # differential equation solution
    x = x0
    v = v0
    for j in range(1,len(time_list)):
        k1 = h * v
        l1 = (-1) * h * const * x
        k2 = h * (v + l1 / 2)
        l2 = (-1) * h * const * (x+ k1 / 2)
        k3 = h * (v + l2 / 2)
        l3 = (-1) * h * const * (x+ k2 / 2)
        k4 = h * (v + l3)
        l4 = (-1) * h * const * (x+ k3)
        x1 = x + (1/6) * (k1+2*k2+2*k3+k4)
        v1 = v + (1/6) * (l1+2*l2+2*l3+l4)
        forth_order_position_list.append(x1)
        forth_order_velocity_list.append(v1)
        x = x1
        v = v1
    
    #graph plot
    plt.plot(time_list, second_order_position_list, label = "2nd order Runge Kutta method for positon")
    plt.plot(time_list, forth_order_position_list, '-.',  label = "4th order Runge Kutta method for postion")
    plt.plot(time_list, second_order_velocity_list,  label = "2nd order Runge Kutta method for velocity")
    plt.plot(time_list, forth_order_velocity_list, '-.', label = "4th order Runge Kutta method for velocity")
    plt.legend()
    plt.show()

elif method == "6":
    #user input
    t0 = float(input("initial time (t0) : "))
    x0 = float(input("initial position (x0) : "))
    v0 = float(input("initial velocity (v0) : "))
    k = float(input("spring constant (k) : "))
    m = float(input("mass of spring (m) : "))
    h = float(input("value of h : "))
        
    #constant calculation
    const = k/m
        
    #creating list for graph
    time_list = [t0]
    for i in range(1,400):
        t = t0 + h*i
        time_list.append(t)
        
    second_order_position_list = [x0]
    second_order_velocity_list = [v0]

    # differential equation solution
    x = x0
    v = v0
    for j in range(1,len(time_list)):
        k1 = h * v
        l1 = (-1) * h * const * x
        k2 = h * (v+l1)
        l2 = (-1) * h * const * (x+k1)
        x1 = x + (1/2) * (k1+k2)
        v1 = v + (1/2) * (l1+l2)
        second_order_position_list.append(x1)
        second_order_velocity_list.append(v1)
        x = x1
        v = v1
    forth_order_position_list = [x0]
    forth_order_velocity_list = [v0]

    # differential equation solution
    x = x0
    v = v0
    for j in range(1,len(time_list)):
        k1 = h * v
        l1 = (-1) * h * const * x
        k2 = h * (v + l1 / 2)
        l2 = (-1) * h * const * (x+ k1 / 2)
        k3 = h * (v + l2 / 2)
        l3 = (-1) * h * const * (x+ k2 / 2)
        k4 = h * (v + l3)
        l4 = (-1) * h * const * (x+ k3)
        x1 = x + (1/6) * (k1+2*k2+2*k3+k4)
        v1 = v + (1/6) * (l1+2*l2+2*l3+l4)
        forth_order_position_list.append(x1)
        forth_order_velocity_list.append(v1)
        x = x1
        v = v1
    #analytical position data
    analytical_position_list = []
    if t0 == 0 and v0 == 0:
        for k in range(len(time_list)):
            analytical_data = x0 * math.cos(math.sqrt(const)*time_list[k])
            analytical_position_list.append(analytical_data)
    else:
        delta = math.atan((-1) * v0 / (x0 * math.sqrt(const))) - math.sqrt(const) * t0
        amplitude = x0 / (math.cos(math.sqrt(const) * t0 + delta))
        for k in range(len(time_list)):
            analytical_data = amplitude * math.cos(math.sqrt(const)*time_list[k] + delta)
            analytical_position_list.append(analytical_data)

    #analytical velocity data
    analytical_velocity_list = []
    if t0 == 0 and v0 == 0:
        for k in range(len(time_list)):
            analytical_data = (-1) * math.sqrt(const) * x0 * math.sin(math.sqrt(const)*time_list[k])
            analytical_velocity_list.append(analytical_data)
    else:
        delta = math.atan((-1) * v0 / (x0 * math.sqrt(const))) - math.sqrt(const) * t0
        amplitude = amplitude / (math.cos(math.sqrt(const) * t0 + delta))
        for k in range(len(time_list)):
            analytical_data = (-1) * math.sqrt(const) * amplitude * math.sin(math.sqrt(const)*time_list[k] + delta)
            analytical_velocity_list.append(analytical_data)    
    
    #graph plot
    plt.plot(time_list, second_order_position_list, label = "2nd order Runge Kutta method")
    plt.plot(time_list, forth_order_position_list, '-.',  label = "4th order Runge Kutta method")
    plt.plot(time_list, analytical_position_list, ':',  label = "analytical value")    
    plt.legend()
    plt.show()

elif method == "7":
    #user input
    t0 = float(input("initial time (t0) : "))
    x0 = float(input("initial position (x0) : "))
    v0 = float(input("initial velocity (v0) : "))
    k = float(input("spring constant (k) : "))
    m = float(input("mass of spring (m) : "))
    h = float(input("value of h : "))
        
    #constant calculation
    const = k/m
        
    #creating list for graph
    time_list = [t0]
    for i in range(1,400):
        t = t0 + h*i
        time_list.append(t)
        
    second_order_position_list = [x0]
    second_order_velocity_list = [v0]

    # differential equation solution
    x = x0
    v = v0
    for j in range(1,len(time_list)):
        k1 = h * v
        l1 = (-1) * h * const * x
        k2 = h * (v+l1)
        l2 = (-1) * h * const * (x+k1)
        x1 = x + (1/2) * (k1+k2)
        v1 = v + (1/2) * (l1+l2)
        second_order_position_list.append(x1)
        second_order_velocity_list.append(v1)
        x = x1
        v = v1
    forth_order_position_list = [x0]
    forth_order_velocity_list = [v0]

    # differential equation solution
    x = x0
    v = v0
    for j in range(1,len(time_list)):
        k1 = h * v
        l1 = (-1) * h * const * x
        k2 = h * (v + l1 / 2)
        l2 = (-1) * h * const * (x+ k1 / 2)
        k3 = h * (v + l2 / 2)
        l3 = (-1) * h * const * (x+ k2 / 2)
        k4 = h * (v + l3)
        l4 = (-1) * h * const * (x+ k3)
        x1 = x + (1/6) * (k1+2*k2+2*k3+k4)
        v1 = v + (1/6) * (l1+2*l2+2*l3+l4)
        forth_order_position_list.append(x1)
        forth_order_velocity_list.append(v1)
        x = x1
        v = v1
    #analytical position data
    analytical_position_list = []
    if t0 == 0 and v0 == 0:
        for k in range(len(time_list)):
            analytical_data = x0 * math.cos(math.sqrt(const)*time_list[k])
            analytical_position_list.append(analytical_data)
    else:
        delta = math.atan((-1) * v0 / (x0 * math.sqrt(const))) - math.sqrt(const) * t0
        amplitude = x0 / (math.cos(math.sqrt(const) * t0 + delta))
        for k in range(len(time_list)):
            analytical_data = amplitude * math.cos(math.sqrt(const)*time_list[k] + delta)
            analytical_position_list.append(analytical_data)

    #analytical velocity data
    analytical_velocity_list = []
    if t0 == 0 and v0 == 0:
        for k in range(len(time_list)):
            analytical_data = (-1) * math.sqrt(const) * x0 * math.sin(math.sqrt(const)*time_list[k])
            analytical_velocity_list.append(analytical_data)
    else:
        delta = math.atan((-1) * v0 / (x0 * math.sqrt(const))) - math.sqrt(const) * t0
        amplitude = amplitude / (math.cos(math.sqrt(const) * t0 + delta))
        for k in range(len(time_list)):
            analytical_data = (-1) * math.sqrt(const) * amplitude * math.sin(math.sqrt(const)*time_list[k] + delta)
            analytical_velocity_list.append(analytical_data)    
    
    #graph plot
    plt.plot(time_list, second_order_velocity_list,  label = "2nd order Runge Kutta method")
    plt.plot(time_list, forth_order_velocity_list, '-.', label = "4th order Runge Kutta method")
    plt.plot(time_list, analytical_velocity_list, ':',  label = "analytical value")
    plt.legend()
    plt.show()