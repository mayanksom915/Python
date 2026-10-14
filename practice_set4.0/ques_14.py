# Merge two text files into a third file.

with open("student.txt", "w") as f:
    f.write("Hello Python")

with open("second.txt", "w") as f:
    f.write("Welcome to CSE")

with open("student.txt", "r") as f:
    data1 = f.read()

with open("second.txt", "r") as f:
    data2 = f.read()

with open("merged.txt", "w") as f:
    f.write(data1 + "\n" + data2)

with open("merged.txt", "r") as f:
    print(f.read())
    
    
# output:
# Hello Python
# Welcome to CSE
