# Q10. Generate squares of numbers from 1 to 10 and store them in a tuple using tuple(x*x for x in range(1, 11)).

squares = tuple(x * x for x in range(1, 11))

print("Squares:", squares)


# output:
# Squares: (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)