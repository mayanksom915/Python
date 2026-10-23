import numpy as np
print("\nThe NUMPY Library Version: ",np.__version__)      # 2.5.4

list1 = [1,2,3,4]
a1=np.array(list1)
a2=np.eye(3)
a3=np.arange(2,10,2)
a4=np.arange(1,10,2)
a5= np.arange(10,21)
a6=np.full((4,3),5)
a7=np.linspace(0,1,5)           # creates evenly spaced numbers btw a given range.
a8=np.ones((4,5))

print("\n1D array: ",a1)
print("\nIdentity Matrix: ",a2) 
print("\nEven Numbers: ",a3)
print("\nOdd Numbers: ",a4)
print("\nPrint a range of numbers: ",a5)
print("\nPrint same element: ",a6)
print("\nOutput of linspace: ",a7)
print("\nOutput: ",a8)


list1=[10,20,30,40]
array=np.array(list1,dtype=float)
array1=np.array(list1,dtype='U32')
print(array)
print(array1)


list1=[10,2.0,30,40,"hello"]
print(np.array(list1))
array=np.array(list1,dtype=object)
print(array)


import numpy as np

# 1. Create an Array

marks = np.array([85, 65, 92, 75, 55])

print("----- Student Marks -----")
print(marks)

# 2. Create an Array Using arange()

print("\n----- Numbers from 1 to 10 -----")
numbers = np.arange(1, 11)
print(numbers)

# 3. Create an Array Using linspace()

print("\n----- Equally Spaced Values -----")
values = np.linspace(0, 100, 5)
print(values)

# 4. Find Array Shape

print("\n----- Shape -----")
print(marks.shape)

# 5. Find Number of Dimensions

print("\n----- Dimensions -----")
print(marks.ndim)

# 6. Count Total Elements

print("\n----- Total Elements -----")
print(marks.size)

# 7. Find Data Type

print("\n----- Data Type -----")
print(marks.dtype)

# 8. Calculate Total Marks

print("\n----- Total Marks -----")
print(np.sum(marks))

# 9. Calculate Average Marks

print("\n----- Average Marks -----")
print(np.mean(marks))

# 10. Find Highest Marks

print("\n----- Highest Marks -----")
print(np.max(marks))

# 11. Find Lowest Marks

print("\n----- Lowest Marks -----")
print(np.min(marks))

# 12. Find Standard Deviation

print("\n----- Standard Deviation -----")
print(np.std(marks))

# 13. Find Index of Highest Marks

print("\n----- Index of Highest Marks -----")
print(np.argmax(marks))

# 14. Sort Marks

print("\n----- Sorted Marks -----")
print(np.sort(marks))

# 15. Filter Marks Greater Than 70

print("\n----- Marks Above 70 -----")
print(marks[marks > 70])

# 16. Use where()

print("\n----- Marks Above 70, Others Replaced with 0 -----")
print(np.where(marks > 70, marks, 0))

# 17. Add 5 Marks to Every Student

print("\n----- After Adding 5 Marks -----")
print(marks + 5)

# 18. Calculate Percentage

print("\n----- Percentage -----")
percentage = (marks / 100) * 100
print(percentage)

# 19. Find Unique Values

print("\n----- Unique Marks -----")
print(np.unique(marks))

# 20. Calculate Cumulative Sum

print("\n----- Cumulative Sum -----")
print(np.cumsum(marks))

# 21. Reshape Array

print("\n----- Reshaped Array -----")
new_marks = np.reshape(marks, (5, 1))
print(new_marks)

# 22. Create a 2D Array

print("\n----- Two-Dimensional Array -----")
matrix = np.array([
[80, 85, 90],
[70, 75, 80],
[90, 95, 100]
])
print(matrix)

# 23. Calculate Column-wise Sum

print("\n----- Column-wise Sum -----")
print(np.sum(matrix, axis=0))

# 24. Calculate Row-wise Sum

print("\n----- Row-wise Sum -----")
print(np.sum(matrix, axis=1))

# 25. Save Array to a File

np.save('student_marks.npy', marks)

print("\nArray saved to student_marks.npy")

# 26. Load Array from a File

loaded_marks = np.load('student_marks.npy')

print("\n----- Loaded Marks -----")
print(loaded_marks)
