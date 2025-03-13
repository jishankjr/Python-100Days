# Walrus Operator

# a = True
print(a:=False)

numbers = [1, 2, 3]

while (n := len(numbers)) > 0:
    print(numbers.pop())


happy = False
print(happy)

print(happy := True)

# foods = list()
# while True:
#     food = input("what food do you like?: ")

#     if food == "quit":
#         break
#     foods.append(food)


foods = list()
while(food := input("What food do you like?: ")) != "quit":
    foods.append(food)