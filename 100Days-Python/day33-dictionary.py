#Python dictionaries
dic= {"Jishank": "Human Being", "Spoon": "Object"}
print(dic["Jishank"])

#Accessing single values and .get()
dic= {
    344: "Jishank",
    56: "Subham",
    576: "Neha",
    669: "Harry" 
}
print(dic[669])
print(dic.get(669))

#Accessing multiple values
info = {'name':'Jishank', 'age':18, 'eligible':True}
print(info.values())

#Accessing keys
info = {'name':'Jishank', 'age':18, 'eligible':True}
print(info.values())

#Accessing key-values pairs
info = {'name':'Jishank', 'age':18, 'eligible':True}
print(info.items())

#Looping key and values
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")