# Q9. Write a Python program to reverse the order of words in a sentence.


sentence = input("Enter a sentence: ")

words = sentence.split()

reverse_words = words[::-1]

result = " ".join(reverse_words)

print("Reversed sentence:", result)

# output:
# Enter a sentence: python is easy language                     
# Reversed sentence: language easy is python