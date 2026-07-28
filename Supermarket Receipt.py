store_name = "RoseMart Supermarket"

name = input("Enter your name: ")
item = input("Enter item purchased: ")
price = float(input("Enter the price of the item: "))

print("============={store_name}================")
print(f"Customer name: {name.title()}")
print(f"Items Purchased: {item.title()}")
print(f"Price: {price:.2f}")
print("=========================================")
