# Read the complete file, reset the pointer using seek(0), and read only the first line.

with open("student.txt", "w", newline="\n") as f:
    f.write("Python is easy\n")
    f.write("Welcome to CSE\n")
    f.write("Learn Python\n")

with open("student.txt", "r") as f:
    print("Complete file:")
    print(f.read())

    f.seek(0)

    print("First line:", f.readline(), end="")
    
# Output:
# Complete file:
# Python is easy
# Welcome to CSE
# Learn Python
# First line: Python is easy