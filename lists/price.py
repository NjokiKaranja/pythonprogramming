products = {}  # initialize an empty dictionary to store the products and their prices

# ask the user to enter product names and prices
while True:
    name = input("Enter product name (or 'done' to finish): ")
    if name == 'done':
        break
    price = input("Enter price: ")
    products[name] = price

# repeatedly ask the user to enter a product name and print the corresponding price
while True:
    name = input("Enter product name (or 'quit' to exit): ")
    if name == 'quit':
        break
    if name in products:
        print(f"The price of {name} is {products[name]}")
    else:
        print(f"{name} is not in the dictionary.")
