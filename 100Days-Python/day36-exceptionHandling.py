# Exception Handling

a = input("Enter the number: ")
print("Multiplication table of {a} is: \n")

try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {a * i}")
except Exception as e:
    print("Error")

# except:
#     print("Error")


print("Some imp lines of code")
print("End of program")


try:
    num = int(input("\nEnter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer!")
except IndexError:
    print("Index Error")