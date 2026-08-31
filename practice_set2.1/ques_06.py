correct_pin = "1234"
account_balance = 5000.0  


entered_pin = input("Enter your 4-digit PIN: ")
amount_to_withdraw = float(input("Enter amount to withdraw: "))


if entered_pin == correct_pin:
    if amount_to_withdraw <= account_balance:
        print("Withdrawal successful! Please collect your cash.")
    else:
        print("Transaction failed! Insufficient account balance.")
else:
    print("Transaction failed! Incorrect PIN.")
