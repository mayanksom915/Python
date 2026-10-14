# Read a text file and create another file containing only lines that contain the word Python.

with open("student.txt", "w", newline="\n") as f:
    f.write("Python is easy\n")
    f.write("Java is useful\n")
    f.write("Python is popular\n")
    f.write("C language is powerful\n")

with open("student.txt", "r") as f:
    lines = f.readlines()

with open("python_lines.txt", "w", newline="\n") as f:
    for line in lines:
        if "Python" in line:
            f.write(line)

with open("python_lines.txt", "r") as f:
    print(f.read(), end="")
    
# Output:
# Python is easy
# Python is popular
    
