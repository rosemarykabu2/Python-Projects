customer_name="Island Asante"

account_balance = 2000

withdrawal_amount = int(input("Enter your withdrawal amount: "))

if withdrawal_amount > 0 and withdrawal_amount < account_balance:
    print("Withdrawal Successful")
else:
    print("Transaction declined")
