correct_username = "admin"
correct_password = "password123"

entered_username = input("Enter Username: ")
entered_password = input("Enter Password: ")

if entered_username == correct_username and entered_password == correct_password:
    print("Login Successful")
else:
    print("Invalid Username or Password.")
