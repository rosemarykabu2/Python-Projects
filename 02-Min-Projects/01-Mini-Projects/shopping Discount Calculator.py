customer_name = input ("Enter your name: ")
total_shopping_amount = float(input("Enter your total shopping amount: "))

if total_shopping_amount >= 500:
    discount = 20
elif total_shopping_amount >=300:
    discount = 10
else:
    discount = 0



if discount > 0:
    discount_amount = (total_shopping_amount * discount) /100
    final_price = total_shopping_amount - discount_amount
    print("===============================")
    print("Shopping Discount Calculator")
    print("================================")

    print(f"Customer Name: {customer_name}")
    print(f"Original Amount: {total_shopping_amount}")
    print(f"Discount_received: {discount}% discount")
    print(f"Final price: {final_price}")
    print("================================================")
    
else:
    print("===============================")
    print("Shopping Discount Calculator") 
    print("================================")
    print("NO DISCOUNT APPLIED")
    print("================================================")
    



