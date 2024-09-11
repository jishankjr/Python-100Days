name = "mango"

length = len(name)
print(length)

print(name[:5])
print(name[0:])

print(name[0:5])    # Include 0 but not 5
print(name[0:3])    # Include 0 but not 3
print(name[0:1])    # Include 0 but not 2
print(name[0:0])    # Include 0 but not 1

print(name[0:-3]) 
print(name[0:len(name)-3]) #print(name[0:5-3])

print(name[-3: -4]) #print(name[2:1])  NO SENSE

print(name[-4:-2])

print(name[1:4])    # Include 0 but not 4