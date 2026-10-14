# Read a file and create a second file with all lines converted to uppercase.

# Q8. Convert all lines to uppercase and save them in another file.

with open("student.txt", "w", newline="\n") as f:
    f.write("Python is easy\n")
    f.write("welcome to cse\n")
    f.write("i am learning python\n")

with open("student.txt", "r") as f:
    data = f.read()

with open("uppercase.txt", "w", newline="\n") as f:
    f.write(data.upper())

with open("uppercase.txt", "r") as f:
    print(f.read(), end="")
    
# output:
# PYTHON IS EASY
# WELCOME TO CSE
# I AM LEARNING PYTHON

