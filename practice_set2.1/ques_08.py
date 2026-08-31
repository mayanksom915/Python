
units = float(input("Enter total electricity units consumed: "))
bill_amount = 0

if units <= 100:
    bill_amount = units * 5
elif units <= 300:
 
    bill_amount = (100 * 5) + ((units - 100) * 7)
else:
    bill_amount = (100 * 5) + (200 * 7) + ((units - 300) * 10)

print(f"Total Electricity Bill: ₹{bill_amount}")
