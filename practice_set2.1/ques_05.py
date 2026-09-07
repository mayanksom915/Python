# Q5. Write a program to determine whether a given year is a leap year.


year = int(input("Enter a year: "))
# A year is leap if it is divisible by 4 but not by 100, 
# OR it must be divisible by 400.
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year: ",year)
else:
    print("not a Leap Year: ",year)
