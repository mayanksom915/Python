# Q11. Write a Python program to find the longest word in a sentence.


sentence = input("Enter a sentence: ")

words = sentence.split()

longest = max(words, key=len)

print("Longest word:", longest)

# output:
# Enter a sentence: Python is an easy language
# Longest word: language