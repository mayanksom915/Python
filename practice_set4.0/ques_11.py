# Find the longest line in a file.

with open("student.txt", "w", newline="\n") as f:
    f.write("Hello\n")
    f.write("Python Programming\n")
    f.write("Welcome to CSE\n")

with open("student.txt", "r") as f:
    lines = f.readlines()

longest = max(lines, key=len)

print("Longest line:", longest, end="")
print("Length:", len(longest.strip()))

# output:
# Longest line: Python Programming
# Length: 18