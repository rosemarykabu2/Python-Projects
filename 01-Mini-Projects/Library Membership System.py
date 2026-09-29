minimum_membership_age = 16
required_membership_fee = 50
maximum_borrowed_books_allowed = 5
member_status = "active"

name=input("Enter your name: ")
age=int(input("Enter your age: "))
fee=int(input("Enter the amount you've paid for membership: "))
books_borrowed=int(input("Enter the number of books borrowed: "))
status=input("What is your membership status (active/inactive): ")

if age >= minimum_membership_age:
    if status == member_status or fee >= required_membership_fee  :
        if books_borrowed <= maximum_borrowed_books_allowed:
            print("Books successfully issued \n Enjoy reading!")
        else:
            print("Sorry, you exceeded the number of books borrowed.")
    else:
        print("Sorry you could not meet our requirement")
else:
    print("Age requirement not met")
        
