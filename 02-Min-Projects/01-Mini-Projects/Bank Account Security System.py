correct_account_number = "A234A"
correct_phone_number = "0508781244"
account_balance = 5000
is_account_active = True

account_number = input("Enter your Account Number: ")
phone_number = input("Enter your phone number: ")
withdrawal_amount = int(input("Enter your withdrawal amount: "))

if account_number == correct_account_number or phone_number == correct_phone_number :
    if is_account_active and withdrawal_amount <= account_balance :
        print("Withdrawal successful")
    else:
        print("Withdrawal denied.")
else:
    print("Account verification failed.")
