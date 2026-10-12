transaction_ids = ["TX101","TX202","TX303","TX404"]
transaction_id = input("Enter your transaction ID: ").upper()

verified = False

for ID in transaction_ids:
    if transaction_id == ID:
        verified = True
        print("Transaction verified successfully.")
        break

if verified == False:
    print("Invalid transaction ID \n Please contact the bank")



