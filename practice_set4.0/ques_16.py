# Read a student marks file and calculate average marks.

with open("student.txt", "w") as f:
    f.write("80\n70\n90\n60")

with open("student.txt", "r") as f:
    marks = f.readlines()

total = 0

for m in marks:
    total = total + int(m)

average = total / len(marks)

print("Total marks:", total)
print("Average marks:", average)

# output:
# Total marks: 300
# Average marks: 75.0