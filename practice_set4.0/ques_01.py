# Read the first 10 characters, display the pointer position, then reset the pointer to 0 and read again.

with open("student.txt", "w") as f:
    f.write("Python is a Programming Language")

with open("student.txt", "r") as f:
    print("First read:", f.read(10))
    print("Pointer position:", f.tell())

    f.seek(0)
    print("Read again:", f.read(10))
    
    
# Output:
# First read: Python is 
# Pointer position: 10
# Read again: Python is 
