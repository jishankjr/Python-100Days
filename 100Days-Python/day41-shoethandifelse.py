a = 330
b = 3303
print("A") if a > b else print("=") if a == b else print("B")

print("9") if a < b else ""

c = 9 if a < b else 0
print(c)

# syntax: result = value_if_true if condition else value_if_false

# if condition:
#     result = value_if_true 
# else:
#     result = value_if_false

a = 3
b = 6
c = 9 if a > b else 0
print(c)

num = int(input("Number: "))

print("Positive") if num > 0 else print("Zero") if num == 0 else print("Negative")