# 1st program:- 
# *
# **
# ***
# ****
# *****

for i in range(1,6):
    print(" * " * i)
    
# 2nd program:-
# 1
# 12
# 123
# 1234
# 12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

# 3rd program:-
# 1
# 22
# 333
# 4444
# 55555
 
for i in range(1,6):
    print(str(i) *i) 
    
# 4th program:-
# 0
# 12
# 345
# 6789

num = 0
for i in range(1,6):
    for j in range(1,i+1):
        print(num,end="")
        num = num+1
    print()
    
# 5th program:-
#     1 
#    1 2 
#   1 2 3 
#  1 2 3 4 
# 1 2 3 4 5 
    
for i in range(1,6):
    print(" " *(5-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
# 6th program:- 
#     1
#    121
#   12321
#  1234321
# 123454321

for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
    
# 7th program:- 
#     1 
#    2 2 
#   3 3 3 
#  4 4 4 4 
# 5 5 5 5 5

for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(1, i + 1):
        print(i, end=" ") 
    print()

