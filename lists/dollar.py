products = {'Product 1': 10, 'Product 2': 20, 'Product 3': 30, 'Product 4': 40, 'Product 5': 50}

# Allow the user to enter a dollar amount
amount = float(input("Enter a dollar amount: "))

# Print all the products whose price is less than that amount
print(f"Products whose price is less than {amount}:")
for product, price in products.items():
    if price < amount:
        print(f"{product}: {price}")
