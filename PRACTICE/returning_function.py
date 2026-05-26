# # Create a function that returns another function
# def greeting():
#     def hello():
#         print("hello ji")
#     return hello
# greet = greeting()
# greet()


# # Create a greeting generator.
# def greeting(name):
#     def wow():
#         print(f"hello {name}")
#     return wow
# greet = greeting("vedant")
# greet() 

# # Create a multiplier generator
# def multi(n):
#     def multip(x):
#         return x*n
#     return multip
# double = multi(2)
# triple = multi(3)
# print(double(5))
# print(triple(5))

# Create a power function generator
def powerr(n):
    def power(x):
        return x**n
    return power
square = powerr(2)
cube = powerr(3)
print(square(5))
print(cube(5))


