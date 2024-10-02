# map, filter and reduce

def cube_n(x):
    return x * x * x


l = [1, 2, 4, 6, 4, 3]
# newl = []
# for item in l:
#     newl.append(cube_n(item))
# print(newl)

# alternately using map function
newl = list(map(cube_n, l))
print(newl)


# FILTER

def filter_function(a):
    return a > 3

new_l = list(filter(filter_function, l))
print(new_l)

# REDUCE

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5] 

# Calculate the sum of the numbers using the reduce function
def mysum(x, y):
  return x + y
# mysum = lambda x, y: x + y
  
sum = reduce(mysum, numbers)

# Print the sum
print(sum)