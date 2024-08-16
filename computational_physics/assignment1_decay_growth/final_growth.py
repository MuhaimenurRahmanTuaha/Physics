# import matplotlib for graph
import matplotlib.pyplot as plt

# method chosing option
print("In which method do you want to solve?")
print("1. Eular method, 2.Taylor series, 3. Comparison graph between Eular and analytical, 4. Comparison graph between Taylor and analytical, 5. Comparison between Eular, Taylor and analytical value ")
method = input("Please type '1' or '2' or '3' or '4' or '5' : ")

# Eular method
if method == "1":
    
    # input part
    t0 = float(input("initial value of time (t0) : "))
    N0 = float(input("initial value of atoms (N0) : "))
    const = float(input("constant value lambda : "))    
    h = float(input("interval (h) : "))
    
    # option chosing
    print("What you want to see?")
    print("1. No of atoms at any time (t) or 2. Graph of Eular's method or 3.Both")
    selection = input("Please type '1' or '2' or '3' : ") 
    if selection == "1":
        # result at t
        t = float(input("final value of time (t) : "))
        n = round((t - t0)/h)
        e = N0
        for k in range(n):
            N = e + h*(const*e)
            e = N 
        print(f"At {t} the no of atoms are {e}")    
    elif selection == "2":
        # creating list for graph's data 
        time_list = []
        eular_series_list = [] # this is for eular solve data

        # for time_list
        for i in range(80):
            time = t0 + 0.1*i
            time_list.append(time)
    
        #for eular_series_list    
        for j in range(len(time_list)):
            n = round((time_list[j] - t0)/h)
            e = N0
            for k in range(n):
                N = e + h*(const*e)
                e = N
            eular_series_list.append(e)
    
        #graph plot
        plt.plot(time_list,eular_series_list, label= "Eular method")
        plt.xlabel("Time")
        plt.ylabel("No of atoms")
        plt.legend()
        plt.show()
    else:
        
        # result at t
        t = float(input("final value of time (t) : "))
        n = round((t - t0)/h)
        e = N0
        for k in range(n):
            N = e + h*(const*e)
            e = N 
        print(f"At {t} the no of atoms are {e}")
        
        # creating list for graph's data 
        time_list = []
        eular_series_list = [] # this is for eular solve data

        # for time_list
        for i in range(80):
            time = t0 + 0.1*i
            time_list.append(time)
    
        #for eular_series_list    
        for j in range(len(time_list)):
            n = round((time_list[j] - t0)/h)
            e = N0
            for k in range(n):
                N = e + h*(const*e)
                e = N
            eular_series_list.append(e)
    
        #graph plot
        plt.plot(time_list,eular_series_list, label= "Eular method")
        plt.xlabel("Time")
        plt.ylabel("No of atoms")
        plt.legend()
        plt.show()

# Taylor series
elif method == "2":
    print("Please keep the initial and final value of t in between 0 to 1")
    # factorial function
    def fact(x):
        if x == 0:
            return 1
        else:
            return x*fact(x-1)

    # input part
    t0 = float(input("initial value of time (t0) : "))
    N0 = float(input("initial value of atoms (N0) : "))
    const = float(input("constant value lambda : "))
    no_of_term = int(input("how many terms do you want to count : "))    

    # option chosing
    print("What you want to see?")
    print("1. No of atoms at any time (t) or 2. Graph of Taylor series or 3.Both")
    selection = input("Please type '1' or '2' or '3' : ") 
    if selection == "1":
        t = float(input("final value of time (t) : "))
        y0 = N0
        for n in range(1,no_of_term+1):
            N = y0 + N0*(const**n)*((t-t0)**n)/fact(n)
            y0 = N
        print(f"Tt time {t} no of atoms are {y0}")
    elif selection == "2":
        #creating list for graph's data
        time1_list = []
        taylor_series_list = []
        for i in range(80):
            x = t0 + 0.01*i
            time1_list.append(x)
            z0 = N0
            for j in range(1,no_of_term+1):
                N1 = z0 + N0*(const**j)*((x-t0)**j)/fact(j)
                z0 = N1
            taylor_series_list.append(z0)
    
        #graph plot
        plt.plot(time1_list,taylor_series_list, label = "Taylor series")
        plt.xlabel("Time")
        plt.ylabel("No of atoms")
        plt.legend()
        plt.show()
    
    else:
        t = float(input("final value of time (t) : "))
        y0 = N0
        for n in range(1,no_of_term+1):
            N = y0 +  N0*(const**n)*((t-t0)**n)/fact(n)
            y0 = N
        print(f"Tt time {t} no of atoms are {y0}")
        #creating list for graph's data
        time1_list = []
        taylor_series_list = []
        for i in range(80):
            x = t0 + 0.01*i
            time1_list.append(x)
            z0 = N0
            for j in range(1,no_of_term+1):
                N1 = z0 + N0*(const**j)*((x-t0)**j)/fact(j)
                z0 = N1
            taylor_series_list.append(z0)
    
        #graph plot
        plt.plot(time1_list,taylor_series_list, label = "Taylor series")
        plt.xlabel("Time")
        plt.ylabel("No of atoms")
        plt.legend()
        plt.show()
elif method == "3":
    # input part
    t0 = float(input("initial value of time (t0) : "))
    N0 = float(input("initial value of atoms (N0) : "))
    const = float(input("constant value lambda : "))    
    h = float(input("interval (h) : "))

    #comparison between Eular and analytical value
    time_list = []
    eular_series_list = [] # this is for eular solve data

    # for time_list
    for i in range(80):
        time = t0 + 0.1*i
        time_list.append(time)

    #for eular_series_list    
    for j in range(len(time_list)):
        n = round((time_list[j] - t0)/h)
        e = N0
        for k in range(n):
            N = e + h*(const*e)
            e = N
        eular_series_list.append(e)
        analytical_list=[] # this list is for the solved equation data
        for l in range(len(time_list)):
            N2 = N0*2.71828182845904523536028747135266249775724709369995**(const*(time_list[l]-t0))
            analytical_list.append(N2)
    
        #graph plot
    plt.plot(time_list,eular_series_list, label= "Eular method")
    plt.plot(time_list,analytical_list, label= "Analytical")
    plt.xlabel("Time")
    plt.ylabel("No of atoms")
    plt.legend()
    plt.show()

elif method =="4":
    print("Please keep the initial and final value of t in between 0 to 1")
    # factorial function
    def fact(x):
        if x == 0:
            return 1
        else:
            return x*fact(x-1)

    # input part
    t0 = float(input("initial value of time (t0) : "))
    N0 = float(input("initial value of atoms (N0) : "))
    const = float(input("constant value lambda : "))
    no_of_term = int(input("how many terms do you want to count : "))    
    #creating list for graph's data
    time1_list = []
    taylor_series_list = []
    for i in range(80):
        x = t0 + 0.01*i
        time1_list.append(x)
        z0 = N0
        for j in range(1,no_of_term+1):
            N1 = z0 + N0*(const**j)*((x-t0)**j)/fact(j)
            z0 = N1
        taylor_series_list.append(z0)
    analytical_list=[] # this list is for the solved equation data
    for l in range(len(time1_list)):
        N2 = N0*2.71828182845904523536028747135266249775724709369995**(const*(time1_list[l]-t0))
        analytical_list.append(N2)    
    #graph plot
    plt.plot(time1_list,taylor_series_list, label = "Taylor series")
    plt.plot(time1_list,analytical_list, label = "Analytical")
    plt.xlabel("Time")
    plt.ylabel("No of atoms")
    plt.legend()
    plt.show()

elif method == "5":
    print("Please keep the initial and final value of t in between 0 to 1")
    # factorial function
    def fact(x):
        if x == 0:
            return 1
        else:
            return x*fact(x-1)

    # input part
    t0 = float(input("initial value of time (t0) : "))
    N0 = float(input("initial value of atoms (N0) : "))
    const = float(input("constant value lambda : "))
    no_of_term = int(input("how many terms do you want to count : "))    
    h = float(input("interval (h) : "))

    #creating list for graph's data
    time1_list = []
    taylor_series_list = []
    for i in range(80):
        x = t0 + 0.01*i
        time1_list.append(x)
        z0 = N0
        for j in range(1,no_of_term+1):
            N1 = z0 + N0*(const**j)*((x-t0)**j)/fact(j)
            z0 = N1
        taylor_series_list.append(z0)
    #for eular_series_list    
    eular_list = []
    for j in range(len(time1_list)):
        n = round((time1_list[j] - t0)/h)
        e = N0
        for k in range(n):
            N = e + h*(const*e)
            e = N
        eular_list.append(e)
    # for analytical list
    analytical_list=[] # this list is for the solved equation data
    for l in range(len(time1_list)):
        N2 = N0*2.71828182845904523536028747135266249775724709369995**(const*(time1_list[l]-t0))
        analytical_list.append(N2)    
    #graph plot
    plt.plot(time1_list,taylor_series_list, label = "Taylor series")
    plt.plot(time1_list,eular_list, label = "Eular method")    
    plt.plot(time1_list,analytical_list, label = "Analytical")
    plt.xlabel("Time")
    plt.ylabel("No of atoms")
    plt.legend()
    plt.show()
    
else:
    print("Please enter a correct option")

