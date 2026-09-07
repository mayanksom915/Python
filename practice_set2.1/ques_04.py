# Q4. Write a program to input marks (0–100) and display the grade: A (90–100), B (75–89), C (60–74), D (40–59), Fail (<40).


marks = float(input("Enter your marks (0-100): "))

if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 75 and marks < 89:
    print("Grade: B")
elif marks >= 60 and marks < 74:
    print("Grade: C")
elif marks >= 40 and marks < 59:
    print("Grade: D")
elif marks >= 0 and marks < 40:
    print("Grade: Fail")
else:
    print("Invalid marks! Please enter a value between 0 and 100.")
