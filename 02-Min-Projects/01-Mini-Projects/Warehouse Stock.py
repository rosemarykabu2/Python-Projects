available_item = "rice"
stock_quantity = 8

item=input("Enter the name of the item: ").lower()
while item != available_item:
    print("Item name is wrong, try again")
    item=input("Enter the name of the item: ").lower()
    
quantity = int(input("Enter the quantity you want to buy: "))
if quantity <= stock_quantity:
    print("Order Confirmed. \n Your items are ready for \n pickup.")
else:
    print("Sorry, insufficient stock \n available")
