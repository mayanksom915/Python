# Q3. Write a Python program to update the salary of an employee in a dictionary.

employee = {
    "Name": "Amit",
    "Salary": 45000
}

print("Before:", employee)

# Update salary
employee["Salary"] = 52000

print("After:", employee)

# output:
# Before: {'Name': 'Amit', 'Salary': 45000}
# After: {'Name': 'Amit', 'Salary': 52000}