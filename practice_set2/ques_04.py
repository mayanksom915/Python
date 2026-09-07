# 4. Input the marks of a student in two subjects. Print "Pass" if both marks are 35 or above. Print "Eligible for Scholarship" if either mark is 90 or above. Print whether the student has not failed using the not operator.


m1 = float(input("Enter the marks of student 1: "))
m2 = float(input("Enter the marks of student 2:"))

if m1 >= 35 and m2 >= 35:
    print("Both students have passed.")
if m1 >= 90 or m2 >= 90:
    print("Eligible for scholarship.")
if not (m1  < 35 or m2 < 35):
    print("not failed")
    
