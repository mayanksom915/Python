# Demonstrate what happens when read() is called twice without using seek().

with open("student.txt", "w") as f:
    f.write("Python is a Programming Language")

with open("student.txt", "r") as f:
    print("First read:", f.read(10))
    print("Second read:", f.read(10))
    
# Output:
# First read: Python is
# Second read:  a Progra