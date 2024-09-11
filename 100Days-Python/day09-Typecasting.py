# Type casting in python
# It is conversion of one data type to another to complete requirement
# ----------------------------------------------------------------------------------------------------

# 1. Explicit type casting : Done by programmer

number = 1
string = "2"
string_number = int(string)
answer1 = number + string_number
print(answer1)
print("Data type of",answer1,"is",type(answer1))


# 2. Explicit type casting : Done by python

number = 1
float = 2.9
answer2 = number + float
print(answer2)
print("Data type of",answer2,"is",type(answer2))