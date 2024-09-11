# Enumerate Function
s = 'hello'
for index, c in enumerate(s):
    print(index, c)
print("\n")

marks = [12, 56, 32, 98, 45, 1, 4]
for index, mark in enumerate(marks):
    print(mark)
    if index == 3:
        print("Jishank, Awesome!")

print("\n")

# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']

for index, fruit in enumerate(fruits):
    print(index, fruit)
print("\n")

# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
print("\n")
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')