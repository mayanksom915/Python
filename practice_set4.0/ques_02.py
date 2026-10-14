# Read 5 characters, skip to another position using seek(), and read the next 10 characters.

with open("student.txt", "w") as f:
    f.write("Python is a Programming Language")

with open("student.txt", "r") as f:
    print("First 5 characters:", f.read(5))

    f.seek(10)

    print("Next 10 characters:", f.read(10))
    
# Output:

# First 5 characters: Pytho
# Next 10 characters: a Progra