# dictionary methods

ep1 = {122: 45, 123: 85, 567: 65, 650: 65}
ep2 = {222: 67, 566: 90}
print("ep1=",ep1,"\nep2=",ep2)

# update()
print("\nupdate()")
ep1 = {122: 45, 123: 85, 567: 65, 650: 65}
ep2 = {222: 67, 566: 90}
ep1.update(ep2)
print(ep1)

# clear
print("\nclear()")
ep1 = {122: 45, 123: 85, 567: 65, 650: 65}
ep1.clear()
print(ep1)

# empty
print("\nempty set")
empt = {}
print(empt)

# pop()
print("\npop()")
ep1 = {122: 45, 123: 85, 567: 65, 650: 65}
ep1.pop(122)
print(ep1)

# popitem()
print("\npopitem()")
ep1 = {122: 45, 123: 85, 567: 65, 650: 65}
ep1.popitem()
print(ep1)

# del
print("\ndel")
ep1 = {122: 45, 123: 85, 567: 65, 650: 65}
# del ep1       -> delete whole dictionary
# print(ep1)    -> now ep1 doesn't exists
del ep1[122]    # -> only delete key 122 
print(ep1)


