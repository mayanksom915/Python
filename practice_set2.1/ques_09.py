num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Giving choices to the user
print("Choose an operation:")
print("+ : Addition")
print("- : Subtraction")
print("* : Multiplication")
print("/ : Division")

choice = input("Enter your choice (+, -, *, /): ")

if choice == "+":
    result = num1 + num2
    print("Result:", result)

elif choice == "-":
    result = num1 - num2
    print("Result:", result)

elif choice == "*":
    result = num1 * num2
    print("Result:", result)

elif choice == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error! Division by zero is not allowed.")

else:
    print("Invalid choice! Please select a valid operator.")
