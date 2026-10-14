# Remove blank lines from a file and save the result to a new file.

with open("student.txt", "w", newline="\n") as f:
    f.write("Python is easy\n")
    f.write("\n")
    f.write("Welcome to CSE\n")
    f.write("\n")
    f.write("Learn Python\n")

with open("student.txt", "r") as f:
    lines = f.readlines()

with open("clean.txt", "w", newline="\n") as f:
    for line in lines:
        if line.strip():
            f.write(line)

with open("clean.txt", "r") as f:
    print(f.read(), end="")
    
#  output:
# Python is easy
# Welcome to CSE
# Learn Python