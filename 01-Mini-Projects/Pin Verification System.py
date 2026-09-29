correct_pin = "4321"
pin = input("Enter your pin: ")

while pin != correct_pin:
    print("Incorrect Pin, Try again")
    pin = input("Enter your pin: ")

if pin == correct_pin :
    print("Pin Verified \n Welcome to your account")
    
