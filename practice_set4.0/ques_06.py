# Create a program that uses tell() to report the pointer position before and after reading.


with open("student.txt", "w", newline="\n") as f:
    f.write("Python is easy")

with open("student.txt", "r") as f:
    print("Before reading:", f.tell())

    print("Read data:", f.read(5))

    print("After reading:", f.tell())
    
# Output:
# Before reading: 0
# Read data: Pytho
# After reading: 5