tuple = (1, 5, "Jishank", 6, 10, 18)       # if tuple = (1) its shows int type. you need to write tuple = (1, ). is the syntax
print(type(tuple), tuple)

#tuple[0] = 10  # shows error because tuple cannot be changed
#print(tuple)

print(tuple[0])
print(tuple[1])
print(tuple[2])

print(tuple[-1])
print(tuple[len(tuple)-1])
print(tuple[5])

if 342 in tuple:
    print("Yes 342 is in tuple")
else:
    print("Not")

