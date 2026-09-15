# 12. Write a function print_table(n) that prints the multiplication table of n.

def print_table(n):
    for i in range(1, 11):
        print(n * i)

print_table(5)