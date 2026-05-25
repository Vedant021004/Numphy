# Create a function that returns another function
def greeting():
    def hello():
        print("hello ji")
    return hello
greet = greeting()
greet()


# Create a greeting generator.
def greeting(name):
    def wow():
        print(f"hello {name}")
    return wow
greet = greeting("vedant")
greet() 

# Create a multiplier generator
def multi(n):
    def multip(x):
        return x*n
    return multip
double = multi(2)
triple = multi(3)
print(double(5))
print(triple(5))


