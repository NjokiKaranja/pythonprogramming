# import opearators

# x=opearators.add(12,34)

# print(x)

# y=opearators.subtract(45,89)
# print(y)

# from opreators import subtract
# from opreators import add

# x=add(23,45)
# y=subtract(89,34)
# print(x)



# import opreators

# x=mathematics.divide(50,2)
# print(x)


# import mathematics
# y=mathematics.multilply(20,30)

# print(y)


# import others
# x=others.cube(9)
# print(x)


# import opreators
# y=opreators.add(7,8)
# print(y)


#get numbers
import operators
import others
import tri

operator= input("Enter operator (+, -, cube, sin): ")
if operator=="cube":
    num=eval(input("enter number"))
    x=others.cube(num)
    print(x)

elif operator=="sin":
    angle=eval(input("enter angle in degrees:"))
    sin_of_angle=tri.get_sin(angle)
    print(sin_of_angle)

else:
    num1 = eval(input("enter number 1:"))
    num2 = eval(input("enter number 2:"))
    operator=input("enter operator:")

    if operator=="+":
        x = operators.add(num1,num2)
        print(x)

    elif operator=="-":
        x = operators.subtract(num1,num2)
        print(x)


    



