# Q8. Write a Python program to create a dictionary from two lists without losing duplicate values.

keys = ["ID", "Name", "Age", "City"]
values = [101, "Ankit", 20, "Delhi"]

student = dict(zip(keys, values))

print(student)

# output:
# {'ID': 101, 'Name': 'Ankit', 'Age': 20, 'City': 'Delhi'}