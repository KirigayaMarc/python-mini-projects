#calculates the final price of an item after a discount is applied.

def calculate_final_price(price,discount_percent):
    discount_amount = price * discount_percent / 100
    final_price = price - discount_amount
    return final_price

original_price = float(input("Enter original price: "))
discount_percentage = float(input("Enter discount percentage: "))
new_price = calculate_final_price(original_price,discount_percentage)
print(new_price)