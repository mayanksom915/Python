numbers = [10, 20, 30, 40, 50]

del numbers[2]
print("After removing third element:", numbers)

del numbers[:]
print("After removing all elements:", numbers)



# output:
# After removing third element: [10, 20, 40, 50]
# After removing all elements: []