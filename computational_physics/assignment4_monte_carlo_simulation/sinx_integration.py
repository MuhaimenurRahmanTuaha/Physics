import math
import random

def function(x):
    return math.sin(x)

number = 0
count = 0
while count<1000000:
    x_coordinate = random.uniform(0, 3.1416)
    y_coordinate = random.uniform(0, 3.1416)
    if y_coordinate <= function(x_coordinate):
        number = number+1
    count = count+1
area_of_box = 3.1416*3.1416
integration = (number/count)*area_of_box
print(integration)

        