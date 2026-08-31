marks = float(input("Enter your marks (0-100): "))

if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 75 and marks < 90:
    print("Grade: B")
elif marks >= 60 and marks < 75:
    print("Grade: C")
elif marks >= 40 and marks < 60:
    print("Grade: D")
elif marks >= 0 and marks < 40:
    print("Grade: Fail")
else:
    print("Invalid marks! Please enter a value between 0 and 100.")
