# 7. Write a function student_result(marks) that accepts a list of marks and returns Total marks, Average marks, Highest marks, Lowest marks.

def student_result(marks):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    return total, average, highest, lowest

print(student_result([80, 75, 90, 85, 70]))