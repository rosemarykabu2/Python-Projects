username = "Rosemond"
password = "python123"

user_name = input("Enter your username: ")
user_password = input("Enter your password: ")

if user_name != username:
        print("User not found")
if user_name == username and user_password != password:
                 print("Incorrect password")
    


if user_name == username and user_password == password:        
        print("Login Successful")

