# File Handeling


# READING A FILE

f = open("day49-myfile.txt", "r")
# print(f)
text = f.read()
print(text)
f.close() 


# WRITING TO A FILE
f = open("day49-myfile2.txt", "w")
f.write("Hello Jishank, how are you")
f.close()

   
# with statement 

with open ('day49-myfile2.txt', 'a') as f:
    f.write("\n ~ I am fine, thanks")