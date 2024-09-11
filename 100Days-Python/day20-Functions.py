# function

def calculation(a, b, c):
    if(a>b and a>c):
        print(a,"is greater!")
    elif(b>c):
        print(b,"is graeter!")
    else:
        print(c,"is greater!")

a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))
calculation(a, b, c)

def multiplication(x):
    pass