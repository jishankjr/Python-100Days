# __name__ == "__main__"

# code in main file

import jishank

jishank.welcome()

# code for jishank module

def welcome():
  print("You are welcome from Jishank")

print(__name__)
if __name__ == "__main__":
  welcome()  
  
#This will print only if this file is run, though jishank is import in main.py, it wont 
# run because for jishank .py __name__ is "__main__" but for main.py it is jishank 
# and the condition is not matched.

 