# 8. Write a function count_vowels(text) that accepts a string and returns the number of vowels in it.

def count_vowels(text):
    count = 0

    for char in text:
        if char.lower() in "aeiou":
            count += 1

    return count

print(count_vowels("Hello World"))