# Q4. Write a Python program to remove a specific key from a dictionary and also remove the last inserted item.

student = {
    "Roll": 101,
    "Name": "Rahul",
    "Branch": "CSE",
    "Sem": 5
}

print("Original dictionary:", student)

# Remove specific key
del student["Branch"]
print("After removing Branch:", student)

# Remove last inserted item
student.popitem()
print("After removing last item:", student)


# output:
# Original dictionary: {'Roll': 101, 'Name': 'Rahul', 'Branch': 'CSE', 'Sem': 5}
# After removing Branch: {'Roll': 101, 'Name': 'Rahul', 'Sem': 5}
# After removing last item: {'Roll': 101, 'Name': 'Rahul'}