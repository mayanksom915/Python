# Q6. Write a Python program to check whether a given key already exists in a dictionary.

student = {
    "Roll": 101,
    "Name": "Rahul",
    "Branch": "CSE",
    "Sem": 5
}

key = input("Enter key: ")

if key in student:
    print("Key Found")
else:
    print("Key Not Found")

# output:
# Enter key: Name
# Key Found