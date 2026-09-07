 # Q7. Write a Python program to find the frequency of each character in a string.



text = input("Enter a string: ")

for c in set(text):
    print(c, ":", text.count(c))


# output:
# Enter a string: hello
# h : 1
# e : 1
# l : 2
# o : 1