text = input("Enter a string: ")

print("First 5 characters:", text[:5])
print("Last 5 characters:", text[-5:])
print("Index 3 to 10:", text[3:11])
print("Every second character:", text[::2])
print("Reverse:", text[::-1])

# output:
# Enter a string: Hello, World!
# First 5 characters: Hello
# Last 5 characters: World
# Index 3 to 10: lo, Wor
# Every second character: Hlo ol!
# Reverse: !dlroW ,olleH