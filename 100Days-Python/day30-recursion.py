# Recursion function in python

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial (n - 1)
    
print(factorial(3))
print(factorial(4))
print(factorial(5))

# fibonacci series

# Fibonacci series Using recursion function

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) 
        
n = int(input("Number: "))
print(f"Fibonacci series upto {n} is: ")
for i in range (n):    
    print(fibonacci(i), end = ", ")