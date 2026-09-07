# Q10. Write a Python program to remove duplicate characters from a string.


text = input("Enter a string: ")
result = ""

for c in text:
    if c not in result:
        result += c

print("After removing duplicates:", result)

# output:
# Enter a string: hello
# After removing duplicates: helo

