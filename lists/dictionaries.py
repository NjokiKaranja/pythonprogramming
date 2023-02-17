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


# def arithmetic(a, b):
#     add = a + b
#     divide = a / b
#     remainder = a % b
#     return add, divide, remainder

# result = arithmetic(5,2)
# print("Addition: ", result[0])
# print("Division: ", result[1])
# print("Remainder: ", result[2])



# dark_theme={
#     "button":"black",
#     "title":"white"
# }

# av=56    #globe scope (inside the function)
#         #global variables =m,y
#         #local variable=x
# # def average(a,b):
# #     av =(a+b)/2
# #     product=av*4
# #     return av

# print(av)



# cars={
#     "model":"ford",
#     "year":1998,
#     "color":"red",
#     "country":"Kenya"



# }

#accessing dictionary items

# print(cars["color"])


# person={
#     "name":"cathy",
#     "age":23,
#     "pets":{
#         "dog":"x",
#         "cat":"y"
#     }

# }



# print(person["pets"]["cat"])

# teams={
#     23:"a"

# }

# profile={}
# profile["username"]="user123"
# profile ["age"]=20
# profile["email"]="njoki123@gmail.com"
# profile["repo"]={
#     "name":"python",
#     "commits":"50"
# }


profile={}
def register():
    username =input("enter username:")
    email=input("enter email:")
    password=input("enter password:")

    #store in dictionary
    profile["username"]=username
    profile["email"]=email
    profile["password"]=password

def get_profile():

    print(profile)

def change_username():
    new_username=input("enter new username")
    profile["username"]=new_username



register()
get_profile()

change_username()
get_profile()










print(profile)


