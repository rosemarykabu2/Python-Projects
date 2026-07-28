minimum_age = 18
ticket_status = "Yes"

name = input("Enter your name: ")
age = int(input("Enter your age: "))
ticket = input("Do you have a ticket? (Yes/No): ")


if age >= minimum_age:
    if ticket == ticket_status:
        print("Entry granted. Enjoy the movie!")
    else:
        print("Entry denied: No valid ticket.")
else:
    print("Entry denied: Age requirement not met.")
