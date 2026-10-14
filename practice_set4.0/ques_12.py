# Find the shortest line in a file.

# Q12. Find the shortest line in a file.

with open("student.txt", "w", newline="\n") as f:
    f.write("Hello Python\n")
    f.write("Hi\n")
    f.write("Programming\n")

with open("student.txt", "r") as f:
    lines = f.readlines()

shortest = min(lines, key=len)

print("Shortest line:", shortest, end="")
print("Length:", len(shortest.strip()))

# output:
# Shortest line: Hi
# Length: 2