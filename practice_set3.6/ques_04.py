# 4. Write a function maximum(a, b) that returns the larger of two numbers.


def maximum(a, b):

    if a > b:
        return a  
    else:
        return b  

num1 = int(input("Enter the value of a: "))
num2 = int(input("Enter the value of b: "))

larger_number = maximum(num1, num2)

print("The larger number is:", larger_number)
