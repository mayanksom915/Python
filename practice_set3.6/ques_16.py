# 16. Student Marks Program
# Create a program using separate functions:
# input_marks(), calculate_total(), calculate_average(), display_result()


def input_marks():
    marks = []

    for i in range(5):
        mark = float(input("Enter marks: "))
        marks.append(mark)

    return marks

def calculate_total(marks):
    return sum(marks)

def calculate_average(total):
    return total / 5

def display_result(total, average):
    print("Total Marks:", total)
    print("Average Marks:", average)

marks = input_marks()
total = calculate_total(marks)
average = calculate_average(total)
display_result(total, average)