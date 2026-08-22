text = input("Enter a string: ")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Swap case:", text.swapcase())
# Remove leading/trailing spaces
clean_text = text.strip()
print("After removing spaces:", clean_text)

# Replace one word with another
print("After replacement:", clean_text.replace("Python", "Java"))

# Split into words
words = clean_text.split()
print("Words:", words)

# Join words using hyphen
print("Joined with hyphen:", "-".join(words))

# output:
# Enter a string:   Python is an easy language
# After removing spaces: Python is an easy language
# After replacement: Java is an easy language
# Words: ['Java', 'is', 'an', 'easy', 'language']
# Joined with hyphen: Java-is-an-easy-language