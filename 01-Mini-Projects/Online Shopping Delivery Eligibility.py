free_delivery_amount = 100
premium_status = "yes"
premium_minimum_amount = 50

name = input("Enter your name: ")
amount = int(input("Enter your shopping amount: "))
membership_status = input("Are you a premium member(yes/no)?: ")

if (amount >= free_delivery_amount) or  (membership_status == premium_status  and amount >= premium_minimum_amount):
    print("Congrats, delivery is free")
else:
    print("Delivery fee applied")


