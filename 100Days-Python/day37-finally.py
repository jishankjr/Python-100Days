# finally clause

try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Error occured")
finally:
    print("I am always executed")


# dealing with function

def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("\nEnter the index: "))
        print(l[i])
        return 1
    except:
        print("Error occured")
        return 0
    finally:
        print("I am always executed")
    
x = func1()
print(x)