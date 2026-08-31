# 1st program:- 

for i in range(1,6):
    print(" * " * i)
    
# 2nd program:-

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

# 3rd program:-
 
for i in range(1,6):
    print(str(i) *i) 
    
# 4th program:-

num = 0
for i in range(1,6):
    for j in range(1,i+1):
        print(num,end="")
        num = num+1
    print()
    
# 5th program:-

for i in range(1,6):
    print(" " *(5-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
# 6th program:- 

for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
    
# 7th program:- 

for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(1, i + 1):
        print(i, end=" ") 
    print()

