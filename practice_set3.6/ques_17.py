# 17. Simple Calculator
# Organise a calculator program using separate functions:
# add(), subtract(), multiply(), divide()


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(add(a, b))

elif operation == "-":
    print(subtract(a, b))

elif operation == "*":
    print(multiply(a, b))

elif operation == "/":
    print(divide(a, b))

else:
    print("Invalid operation")