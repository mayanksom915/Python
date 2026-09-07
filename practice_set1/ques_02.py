# 2. Swap the values of two variables using both the traditional method and Python's tuple unpacking.


# TRADITIONAL METHOD
a=10
b=20
temp=a
a=b
b=temp
print("a = ",a)
print("b = ",b)

# PYTHON TUPLE UNPACKING
a=10
b=20
a,b=b,a
print("a = ",a)
print("b = ",b)