# Read a file and write its lines in reverse order to another file.

with open("student.txt", "w", newline="\n") as f:
    f.write("First line\n")
    f.write("Second line\n")
    f.write("Third line\n")

with open("student.txt", "r") as f:
    lines = f.readlines()

with open("reverse.txt", "w", newline="\n") as f:
    for line in reversed(lines):
        f.write(line)

with open("reverse.txt", "r") as f:
    print(f.read(), end="")
    
# output:
# Third line
# Second line
# First line
