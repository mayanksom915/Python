# Display the pointer position after every readline() operation.


with open("student.txt", "w", newline="\n") as f:
    f.write("Python is easy\n")
    f.write("Welcome to CSE\n")
    f.write("Learn Python\n")

with open("student.txt", "r") as f:
    print(f.readline(), end="")
    print("Pointer position:", f.tell())

    print(f.readline(), end="")
    print("Pointer position:", f.tell())

    print(f.readline(), end="")
    print("Pointer position:", f.tell())
    
# Output:
# Python is easy
# Pointer position: 15
# Welcome to CSE
# Pointer position: 30
# Learn Python
# Pointer position: 43
