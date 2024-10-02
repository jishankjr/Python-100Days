# readline()

f = open('day50-myfile.txt', 'r')
while True:
    line = f.readlines()
    if not line:
        break      
    print(line)
f.close()

f1 = open('day50-myfile2.txt', 'r')
i = 0
while True:
    i = i + 1
    line = f1.readline()
    if not line:
        break 
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of student {i} in maths is: {m1}")
    print(f"Marks of student {i} in english is: {m2}")
    print(f"Marks of student {i} in science is: {m3}")
    print(line)
f1.close()

# writelines()
f3 = open('day50-myfile3.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f3.writelines(lines)
f3.close()