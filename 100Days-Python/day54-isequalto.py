# 'is' vs '=='

a = 4
b = "4"
print(a is b)   # compare exact location of the object in memory
print(a == b)   # compare value

a = 3
b = 3
print(a is b)   
print(a == b)   

print("\n~Tuple")
a = (1, 2)
b = (1, 2)
print(a is b)   
print(a == b)  

print("\n~List")
a = [1, 2, 43]
b = [1, 2, 43]
print(a is b)   
print(a == b)   

print("\n~None")
a = None
b = None
print(a is b)   
print(a is None)   # compare exact location of the object in memory
print(a == b)  