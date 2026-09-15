# 18. Electricity Bill
# Create a program using functions:
# get_units(), calculate_bill(), display_bill()

def get_units():
    units = float(input("Enter units consumed: "))
    return units

def calculate_bill(units):
    if units <= 100:
        bill = units * 5

    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)

    else:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    return bill

def display_bill(bill):
    print("Electricity Bill:", bill)

units = get_units()
bill = calculate_bill(units)
display_bill(bill)