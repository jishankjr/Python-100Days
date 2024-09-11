# valueError
num = int(input("Enter number between 5 to 10: "))
if num < 5 or num > 10:
    raise ValueError("Number should be between 5 to 10!")

# passing "quit" and other number and blocking rest
num = input("Enter number between 5 to 10: ")

if num =="quit":
    print("")
else:
    num = int(num)
    if num < 5 or num > 10:
        raise ValueError("Number should be between 5 to 10!")

# custom error 

class CustomError(Exception):
    """Custom Exception raised for specific errors."""
    pass

def evenOddCheck(num):
    if num == 0:
        raise CustomError("Number should not be 0")
    elif num < 0:
        raise CustomError("Number cannot be negative")
    else:
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
try:
    num = int(input("Number: "))
    evenOddCheck(num)
except CustomError as e:
    print(f"CustomError: {e}")








