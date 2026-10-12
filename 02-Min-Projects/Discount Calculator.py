def calculate_price(price):
    if price > 100:
        result = price * 0.10
        
        return price - result
    else:
        return price

final_price = calculate_price(80)

print(final_price)
