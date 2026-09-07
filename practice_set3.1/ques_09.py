# Q9. Create variables: A = 245, B = 37, C = -128.75. Calculate A² using pow(), find the absolute value of C, print the maximum and minimum among A, B, and abs(C), calculate the average of all three numbers, and display every result with appropriate labels.


A = 245
B = 37
C = -128.75

square_A = pow(A, 2)
absolute_C = abs(C)
maximum = max(A, B, C)
minimum = min(A, B, C)
average = (A + B + C) / 3

print("A² =", square_A)
print("Absolute value of C =", absolute_C)
print("Maximum =", maximum)
print("Minimum =", minimum)
print("Average =", average)