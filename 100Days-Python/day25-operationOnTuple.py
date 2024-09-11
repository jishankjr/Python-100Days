countries = ("Nepal", "Pakistan", "Bangladesh", "Hongkong", "China")
temp = list(countries)
temp.append("Russia")
temp.pop(1)
temp[1] = "India"
countries = tuple(temp)
print(countries)


countries1 = ("Nepal", "Pakistan", "Bangladesh")
countries2 = ("Hongkong", "China")
countries = countries1 + countries2
print(countries)


tuple1 = (0, 1, 2, 3, 2, 32, 1, 3, 2, 3)
result = tuple1.count(3)
result1 = tuple1.index(3)
result2 = tuple1.index(3, 4, 8)
print(len(tuple1))
print(result)
print(result1)
print(result2)


