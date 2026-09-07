# 2. Write a program that takes an integer as input and applies the following operations one by one: += 10, -= 5, *= 2, /= 3. Display the value after each operation.

x=int(input("Enter first number: "))
x+=10
print("After adding value of x is:",x)
x-=5
print("After subtracting value of x is:",x)
x*=2
print("After multiplying value of x is:",x)
x/=3
print("After dividing value of x is:",x)