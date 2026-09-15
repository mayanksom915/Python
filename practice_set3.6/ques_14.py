# 14. Write a function count_numbers(numbers) that accepts a list and returns the number of positive numbers, negative numbers, and zeros.

def count_numbers(numbers):
    positive = 0
    negative = 0
    zero = 0

    for n in numbers:
        if n > 0:
            positive += 1
        elif n < 0:
            negative += 1
        else:
            zero += 1

    return positive, negative, zero

print(count_numbers([10, -5, 0, 7, -2, 0, 8]))