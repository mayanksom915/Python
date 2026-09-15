# 9. Write a function reverse_number(n) that returns the reverse of a number.

def reverse_number(n):
    return int(str(n)[::-1])

print(reverse_number(12345))