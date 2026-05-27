
# import exper as exp

# def change(puuchi):
#     def wrapper():
#         print("01")
#         puuchi()
#     return wrapper

# @change
# def printer():
#     print("employee")

# printer()
# @change
# def trip():
#    print("hima")

# trip()


def decor(add):

    def wrapper():

        result = add()

        num3 = int(input("Enter third number: "))

        result = result + num3

        return result

    return wrapper


@decor
def add():

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 + num2

    return result


print("Answer is :", add())