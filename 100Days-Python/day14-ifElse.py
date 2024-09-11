# if else statements

""" if
    if-else
    if-else-elif
    nested if-else-elif """

# age = int(input("Enter your age: "))
# print("Your age is",age)

# if(age>=18):
#     print("You are eligible to vote!")

# else:
#     print("You are not eligible to vote")
# print("hi")


age = int(input("Enter your age: "))

if(age>17):
    if(18 < age < 30):
        print("You are adult")
    elif(30 < age < 50):
        print("You are uncle")
    else:
        print("You are old")
elif(age == 18): 
    print("You are 18")
else:
    print("You are baby")
    


