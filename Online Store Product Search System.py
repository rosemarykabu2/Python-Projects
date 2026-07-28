products = ["laptop","phone","tablet","watch"]
product_name = input("Enter the product you are looking for: ")

for product in products:
    if product_name == product:
       break
       print(f"Product found! \n {product_name} is available")
    else:
        print("Sorry, product not available")
