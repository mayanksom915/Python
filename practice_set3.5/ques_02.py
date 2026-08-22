my_set = {10, 20, 30, 40, 50}

print("Original set:", my_set)

my_set.remove(20)
print("After remove(20):", my_set)

my_set.discard(30)
print("After discard(30):", my_set)

my_set.pop()
print("After pop():", my_set)


# output:
# Original set: {40, 10, 50, 20, 30}
# After remove(20): {40, 10, 50, 30}
# After discard(30): {40, 10, 50}
# After pop(): {40, 10}