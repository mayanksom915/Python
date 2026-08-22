text = input("Enter a string: ")

upper = lower = digits = spaces = special = 0

for c in text:
    if c.isupper():
        upper += 1
    elif c.islower():
        lower += 1
    elif c.isdigit():
        digits += 1
    elif c.isspace():
        spaces += 1
    else:
        special += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)


# output:
# Enter a string: Hello World! 123  
# Uppercase letters: 1
# Lowercase letters: 8
# Digits: 3
# Spaces: 1
# Special characters: 1