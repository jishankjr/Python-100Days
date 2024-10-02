# decorators

def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thank for using thsis function")
    return mfx
    
@greet
def hello():
    print("Hello World")

hello()
# greet(hello)()

print("\n\nadd()")
# add

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thank for using thsis function")
    return mfx
    

@greet
def hello():
    print("Hello World")

# @greet
def add(a, b):
    print(a+b)
    
hello()
# greet(hello)()
greet(add)(1, 2)