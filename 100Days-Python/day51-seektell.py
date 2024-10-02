# seek() tell()

f = open('day51-myfile.txt', 'r')

# with open('day51-myfile.txt', 'w') as f:

print(type(f))
# Move to the 10th byte in the file
f.seek(10)

print(f.tell())
# Read the next 5 bytes
data = f.read(5)
print(data)

# truncate() 

with open('day51-myfile2.txt', 'w') as f1:
    f1.write("Hello World3!")
    f1.truncate(6)

with open('day51-myfile2.txt', 'r') as f1:
    print(f1.read())