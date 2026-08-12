student = ("Mayank", 20, "BCA")
print("Packed tuple:", student)
name, age, course = student
print("Name:", name)
print("Age:", age)
print("Course:", course)
numbers = (10, 20, 30, 40, 50)
a, *b, c = numbers
print("First:", a)
print("Middle:", b)
print("Last:", c)


# output:
# Packed tuple: ('Mayank', 20, 'BCA')
# Name: Mayank
# Age: 20                                               
# Course: BCA
# First: 10
# Middle: [20, 30, 40]
# Last: 50