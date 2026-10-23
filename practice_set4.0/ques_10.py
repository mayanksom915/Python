# Count the frequency of each word in a text file.

with open("student.txt", "w", newline="\n") as f:
    f.write("Python is easy\n")
    f.write("Python is useful\n")

with open ("student.txt", "r") as f:
    text = f.read()