minimum_age = 18
is_room_available = True
id_valid = "yes"

name = input("Enter your name: ")
age = int(input("Enter your age: "))
id_check = input("Is your ID valid (Yes/No): ")



if age >= minimum_age:
    if is_room_available:
        if id_check == id_valid:
            print("Room booked, congrats")
        else:
            print("Id is invalid")
    else:
        print("Sorry, rooms are occupied")
else:
    print("Age requirement not met")


    
