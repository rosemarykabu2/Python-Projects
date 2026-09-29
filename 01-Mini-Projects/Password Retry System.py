correct_password = "python123"
password = input("Enter your password: ")

count = 0
while password != correct_password:
    print("Wrong Try again!")
    password = input("Enter your password again: ")
if password ==  correct_password :
    print("Login Successful")
    
    
