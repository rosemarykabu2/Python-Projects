item_name = "Notebook"
price = 15

user_input = int(input("How many notebook do you want to buy: "))

total_cost = price * user_input

print("=====================")
print("Receipt")
print("=====================")

print(f"Item: {item_name}")
print(f"Price per notebook: {price}")
print(f"Quantity: {user_input}")
print(f"Total cost: {total_cost}")

print("==================================")
