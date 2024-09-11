print("for loop with else")

for i in range(5):
    print(i)
else:
    print("Sorry no i")

print("\nIn empty list:")
for i in []:
    print(i)
else:
    print("Sorry no i")


print("\nelse mean loop is not break, loop is finished")
for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("Sorry no i")

print("\nelse with while loop")
i = 0
while i < 7:
    print(i)
    i = i + 1
    if i == 4:
        break
else:
    print("No i")

print("\nMore understanding")
for x in range(5):
    print("Iteration no {} in for loop".format(x+1))
else:
    print("Else block in loop")
print("End of loop")


















