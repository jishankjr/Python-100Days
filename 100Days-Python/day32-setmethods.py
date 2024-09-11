#Union
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2))

#Intersection
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.intersection(s2))

#Update
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
s1.update(s2)
print(s1)

#intersection_update()
cities1 = {"Tokyo", "Madrid","Berlin", "Dehli"}
cities2 = {"Tokyo", "Seoul","Kabul", "Madrid"}
cities1.intersection_update(cities2)
print(cities1)

#symmetric_difference()
cities1 = {"Tokyo", "Madrid","Berlin", "Dehli"}
cities2 = {"Tokyo", "Seoul","Kabul", "Madrid"}
cities3 = cities1.symmetric_difference(cities2)
print(cities3)

#difference()
cities1 = {"Tokyo", "Madrid","Berlin", "Dehli"}
cities2 = {"Tokyo", "Seoul","Kabul", "Madrid"}
cities3 = cities1.difference(cities2)
print(cities3)

#isdisjoint()
cities1 = {"Tokyo", "Madrid","Berlin", "Dehli"}
cities2 = {"Tokyo", "Seoul","Kabul", "Madrid"}
print(cities1.isdisjoint(cities2))

#issuperset()
cities1 = {"Tokyo", "Madrid","Berlin", "Dehli", "Seoul", 
"Kabul"}
cities2 = {"Tokyo", "Seoul","Kabul", "Madrid"}
print(cities1.issuperset(cities2))

#issubset()
cities1 = {"Tokyo", "Madrid","Berlin", "Dehli"}
cities2 = {"Tokyo", "Madrid","Berlin", "Dehli", "Seoul", 
"Kabul", "Nepal", "Pakistan"}
print(cities1.issubset(cities2))

#add()
cities1 = {"Tokyo", "Madrid","Berlin", "Dehli"}
cities1.add("Nepal")
print(cities1)

#remove
cities1 = {"Tokyo", "Madrid","Berlin", "Dehli"}
cities1.remove("Tokyo")
print(cities1)

#discard
cities1 = {"Tokyo", "Madrid","Berlin", "Dehli"}
cities1.discard("Tokyo")
print(cities1)

#pop()
cities1 = {"Tokyo", "Madrid","Berlin", "Dehli"}
item = cities1.pop()
print(cities1)
print(item)

#del set_name
cities1 = {"Tokyo", "Madrid","Berlin", "Dehli"}
del cities1

#clear()
cities1 = {"Tokyo", "Madrid","Berlin", "Dehli"}
cities1.clear()
print(cities1)

#if use in set
cities1 = {"Tokyo", "Madrid","Berlin", "Dehli"}
if "Tokyo" in cities1:
    print("Yes")
else:
    print("No")