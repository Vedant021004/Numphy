# Store a function inside a variable and call it.
# def first():
#     print("ki haal hai bhai")
# call = first
# call()

# Pass a function as an argument to another function.
# def wow(name):
#     return f"hello {name}"
# def check(a,b):
#     return a(b)
# print(check(wow,"vedant"))

# # Create a calculator using functions as arguments
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b

# def calculator(bhai,a,b):
#     return bhai(a,b)
# print(add(2,2))
# print(sub(4,2))
# print(mul(6,2))
# print(div(8,2))


# def fun1():
#     print("hello bhai")
# def fun2():
#     print("hello bhai ji")

# fun_list = [fun1,fun2]
# for func in fun_list:
#     func()

# def check_balance():
#     # In a real app, this would check a database or variable
#     print("\n💰 Your current balance is: $100.00")

# def deposit_money():
#     amount = input("\n💵 Enter amount to deposit: ")
#     print(f"✅ Successfully deposited ${amount}.")

# def withdraw_money():
#     amount = input("\n🏧 Enter amount to withdraw: ")
#     print(f"✅ Successfully withdrew ${amount}.")

# def exit_system():
#     print("\n👋 Thank you for using our system. Goodbye!")
#     # Returning False will tell our main loop to stop running
#     return False


# 1
def call(name):
    
    print("mera naam ",name)

call1 = call 
call1("vedant")     

# 2
def argument(type):
    print(type)
def passe(fun,value):
    return fun(value)
    
print(passe(argument,"jaanu"))

# 3

def first():
    print("main pehla hoon ji")
def second():
    print("main doosra hoon ji")
def third():
    print("main third hoon ji")

fun = [first(), second(), third()]
for i in fun:
    print(fun())   



# Assign one function to multiple variables
def get_coordinates():
    # Returns a tuple behind the scenes
    return 10, 25, 50

# Assign to multiple variables by unpacking
x, y, z = get_coordinates()

print(x) # Output: 10
print(y) # Output: 25
print(z)
    
##---##
def calculator():
        return 5,25,30
x, y, z = calculator()
print(x)
print(y)
print(z)