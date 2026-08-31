marks = float(input("Enter student marks: "))
attendance = float(input("Enter attendance percentage: "))


if marks >= 85 and attendance >= 75:
    print("Congratulations! The student is eligible for the scholarship.")
else:
    print("Sorry! The student is not eligible for the scholarship.")
