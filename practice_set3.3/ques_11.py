sentence = input("Enter a sentence: ")

words = sentence.split()

longest = max(words, key=len)

print("Longest word:", longest)

# output:
# Enter a sentence: Python is an easy language
# Longest word: language