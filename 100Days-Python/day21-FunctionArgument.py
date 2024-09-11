# # default arguments
# def average(a = 8, b = 8):
#     print("The average is ", (a+b)/2)

# average(3, 4)


# def intro(fn ,ln = "rimal"):
#     print("Hello, ",fn,ln)
# intro("jishank")

#requirement argument, in above code we cant run if last one doesnt have value

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)

c = average(1,2,3,4)
print(c)
