account = {
    "name":"Rose",
    "balance":1000,
    "pin":1234
    }
user_pin = int(input("Enter your pin: "))

if user_pin == account["pin"]:
    print("Pin Correct. Welcome,Rose!")
    print(f"Your current balance: {account['balance']}")

    withdraw_amount = int(input("Enter amount to withdraw: "))
    if withdraw_amount <= account['balance']:
        account['balance'] = account['balance'] - withdraw_amount
        print(f"Your new balance:{account['balance']}")
    else:
        print("Insufficient balance")
        
    deposit_amount = int(input("Enter amount to deposit: "))
    account['balance'] = account['balance'] + deposit_amount
    print(f"Your account was deposited with {deposit_amount}, New balnce: {account['balance']}")
    
else:
    print("Incorrect Pin. Access denied")

