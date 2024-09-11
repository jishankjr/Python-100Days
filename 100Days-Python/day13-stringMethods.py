name = "hi, I am The Jishank Rimal. i am a developer."

# 1. upper()  -> Change string to uppercase
print(name.upper())

#2. lower()     -> Change string to lowercase
print(name.lower())

#3. rstrip()    -> removes special characters we want but only that are at the end
print(name.rstrip("!"))

# 4. replace     -> replce required string with another
print(name.replace("Jishank","Tony"))

# 5. split()    -> splits the string separated with spaces in listed form
print(name.split(" "))

# 6. capitalize()   -> capitalize the first letter
print(name.capitalize())

# 7. center()    -> put string in center
print(name.center(100))
print(len(name))
print(len(name.center(100)))

# 8. count()    -> to count the number of string
print(name.count("Jishank"))

# 9. endswith()     -> To know confirm what the string ends with
print(name.endswith("."))
print(name.endswith("m", 0, 8)) # -> doesn't start with 0, upto 8

# 10. find()    -> gives the index of te word i.e. the number of position where the character is 
# but only the first one found. If no word then return -1
print(name.find("am"))

# 11. isalnum()     -> confirms string is starts and ends with either A-Z or a-z or 0-9 
names = "WelcomeToTheConsole"
print(names.isalnum())

# 12. isalpha()     -> only a-z or A-Z
print(names.isalpha())

# 13. islower()     -> confirms if string is lowercase
print(names.islower())

# 14. isprintable()     -> True is string is correct and be printed else false
print(name.isprintable())
namess = "Hi \n"
print(namess.isprintable())

# 15.  isspace()    -> only space in string
space = " "
print(space.isspace())

# 16. istitle   -> first letter of each string is capital 
title = "Is Mocking Bird"
print(title.istitle())

# 17. isupper   -> string is uppercase or not
st = "WHO"
print(st.isupper())

# 18. startswith()   -> to confirm the first string
mess = "Jishank Rimal is powerful."
print(mess.startswith("Jishank"))

# 19. swapcase()    -> uppercase to lowercase and vice-versa
print(mess.swapcase())

# 20. title()   -> first letter of each string capital
print(mess.title())