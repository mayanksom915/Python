# Separate even and odd numbers stored in a file into two different files.

with open("student.txt", "w") as f:
    f.write("10 15 20 25 30 35")

with open("student.txt", "r") as f:
    numbers = f.read().split()

with open("even.txt", "w") as e:
    with open("odd.txt", "w") as o:
        for n in numbers:
            if int(n) % 2 == 0:
                e.write(n + "\n")
            else:
                o.write(n + "\n")

with open("even.txt", "r") as e:
    print("Even numbers:")
    print(e.read(), end="")

with open("odd.txt", "r") as o:
    print("Odd numbers:")
    print(o.read(), end="")
    
# output:
# Even numbers:
# 10
# 20
# 30
# Odd numbers:
# 15
# 25
# 35