
my_list = [10, 20, 10, 30, 20, 40, 30]

# Convert list into set to remove duplicates
my_set = set(my_list)

# Convert back to list
new_list = list(my_set)

print("Original list:", my_list)
print("List after removing duplicates:", new_list)

# output:
# Original list: [10, 20, 10, 30, 20, 40, 30]
# List after removing duplicates: [40, 10, 20, 30]