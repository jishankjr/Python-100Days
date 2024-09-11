list = [5, 3, 10, 1, 6, 2, 8, 9, 4]
print(list)
list.append(7) # 1. append() = adds character you want to add
print(list)
list.sort()     # 2. sort() = sorts ascending to descending
print(list)
list.sort(reverse=True)     # 3. sort(reverse=Ture) = sort() = sorts descending to ascending
print(list)
list.reverse()          # 4. reverses the string
print(list)
print(list.index(4))        # 5. index() = gives position of character

print(list.count(1))    # 6. count() = counts character

m = list.copy()         # 7. copy() = copies list but not change if other change
m[0] = 0
print(list)

# m = list
# m[0] = 10
# print(list)

list.insert(1, 1000)        # 8. insert() = to insert character by index number
print(list)

n = [900, 800, 1100]        # 9. extend() = open list, bring n and print altogether
list.extend(n)
print(list)

# to concatenate
k = list + n
print(k)
