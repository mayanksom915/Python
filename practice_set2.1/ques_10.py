# Q10. WAP to validate a user's username and password. If both are correct, display "Login Successful"; otherwise, display "Invalid Username or Password".

correct_username = "admin"
correct_password = "password123"

entered_username = input("Enter Username: ")
entered_password = input("Enter Password: ")

if entered_username == correct_username and entered_password == correct_password:
    print("Login Successful")
else:
    print("Invalid Username or Password.")
