# Local variable vs Global Variable

x = 4           # Global variable
print(x)

def hello():
    x = 5       # Local variable
    print(f"The local x is {x}")
    print("Hello Jishank")

print(f"The Global x is {x}")
hello()
print(f"The Global x is {x}")


print("\n\nGlobal Keyword\n")

x = 4           # Global variable
print(x)

def hello():
    global x
    x = 5       # Now changes global variable
    print(f"The local x is {x}")
print(f"The Global x is {x}")
hello()
print(f"The Global x is {x}")