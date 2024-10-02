def double(x):
    return x*2
print(double(5))

# lambda function
double = lambda x: x * 2
print("Double of is", double(5))

square= lambda num: num * num
print("Square is", square(5))

cube = lambda num: num * num * num
print("Cube is", cube(5))

avg = lambda x, y, z: (x + y + z) / 3
print("Average is", avg(3, 5, 10))


# function of function
def appl(fx, value):
    return 6 + fx(value)
print(appl(cube, 2))

# Alternately
def appl(fx, value):
    return 6 + fx(value)
print(appl(lambda a:a*a*a, 2))