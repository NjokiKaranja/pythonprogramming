# cars = {
#     "model": "audi",
#     "year": 1967

   

# }
# print(cars["model"])
# cars.update({"year":1965})
# world={
#     "country1":{"name":"Kenya"},
#     "country2":{"name":"Uganda"},
#     "country3":{"name":"Sudan"}


# }
# print(world["country3"]["name"])


# def my_function(first_name):
#     print(first_name+"hello")
# my_function("Njoki")
# my_function("Java")

# def greet_user():
#     name = input("What's your name? ")
#     print("Hello, " + name)


# greet_user()


def arithmetic(a, b):
    add = a + b
    divide = a / b
    remainder = a % b
    return add, divide, remainder

result = arithmetic(5,2)
print("Addition: ", result[0])
print("Division: ", result[1])
print("Remainder: ", result[2])












