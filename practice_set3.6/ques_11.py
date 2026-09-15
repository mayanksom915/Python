# 11. Write a function check_prime(n) that returns whether a number is prime or not.

def check_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(check_prime(7))