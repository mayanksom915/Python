# Count the frequency of each word in a text file.

with open("student.txt", "w", newline="\n") as f:
    f.write("Python is easy\n")
    f.write("Python is useful\n")

with open("student.txt", "r") as f:
    words = f.read().split()

for word in sorted(set(words)):
    print(word, ":", words.count(word))
    
# output:
# Python : 2
# easy : 1
# is : 2
# useful : 1