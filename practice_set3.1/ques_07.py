# Q7. Write a program to input an integer, a float, and a complex number, then display their values and data types.


a = int(input("Enter first number: "))
b = float(input("Enter second number: "))
c = complex(input("Enter third number: "))

print("Integer",a,"Data",type(a))
print("Float",b,"Data",type(b))
print("Complex",c,"Data",type(c))