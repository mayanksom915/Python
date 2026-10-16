# Read a student marks file and calculate average marks.

with open("student.txt", "w") as f:
    f.write("80\n70\n90\n60")

with open("student.txt", "r") as f:
    marks = f.readlines()

