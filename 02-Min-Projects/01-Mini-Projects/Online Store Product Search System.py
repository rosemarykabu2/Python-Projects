products = ["laptop","phone","tablet","watch"]
product_name = input("Enter the product you are looking for: ").lower()

found = False

for product in products:
    if product_name == product:
        found = True
        print(f"Product found! \n {product_name} is available")
        break

if found == False:
    print("Sorry product is unavailable")
