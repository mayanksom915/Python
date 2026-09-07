# Q4. Write a Python program to check whether two sets are disjoint or not. Two sets are disjoint if they have no elements in common.

set1 = {10, 20, 30}
set2 = {40, 50, 60}

# Check whether sets are disjoint
if set1.isdisjoint(set2):
    print("The sets are disjoint.")
else:
    print("The sets are not disjoint.")


# output:
# The sets are disjoint.

   
# set1 = {10, 20, 30}
# set2 = {40, 50, 60}

# # Check whether sets are disjoint
# print(set1.isdisjoint(set2))