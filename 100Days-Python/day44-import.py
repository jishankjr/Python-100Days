import math
square_root = math.sqrt(25)
print(square_root)

import math as m
r = int(input("Radius: "))
area = m.pi * r * r
print("Area of circle of radius",r,"is",area)
print("Value of pi =",m.pi)

from math import sqrt
sq = sqrt(16)
print(sq)
# print(pi) doesn't print because it is not imported

from math import sqrt,pi
sq = sqrt(16)
print(sq)
print(pi)
 
# from math import *
# print(pi)
# print(sqrt(36))
# Create complexities because all the functions are imported

# to know more functions of a module
import math
print(dir(math))

# the function of math 'nan'
import math
print(math.nan, type(math.nan))
