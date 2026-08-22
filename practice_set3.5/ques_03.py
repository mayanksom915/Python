
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Union:", set1 | set2)

# Intersection
print("Intersection:", set1 & set2)

# Difference
print("Difference:", set1 - set2)

# Symmetric Difference
print("Symmetric Difference:", set1 ^ set2)


# output: 
# Union: {10, 20, 30, 40, 50, 60}
# Intersection: {40, 30}
# Difference: {10, 20}
# Symmetric Difference: {10, 20, 50, 60}