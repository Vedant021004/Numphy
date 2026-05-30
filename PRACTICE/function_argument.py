# def naam(name="vedant", age=21):

#     new_name = input("Enter name (press enter for default): ")
#     new_age = input("Enter age (press enter for default): ")

#     if new_name:
#         name = new_name

#     if new_age:
#         age = int(new_age)

#     print(name)
#     print(age)

#     return name, age


# print(naam())



# Create a function using keyword arguments.

# def student_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# # Calling the function with keyword arguments
# student_info(name="Rahul", age=21, roll_no = 122, course="Python")


# def greet(greeting, **kwargs):
#     print(greeting)
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")

# greet("Hello", name="Amit", city="Mumbai")


# def hum(vedrid , **kwargs):
#     print(vedrid)
#     for k, c in kwargs.items():
#         print(f"{k} = {c}")

# hum("vedant", name ="vedant", rollno = 36, age = 21, course = "python")



# def calcate(*args):
#     total = 0
#     for i in args:
#         total = total + i
        
#     return total
        
# print(calcate(1,2,3,4,5,6,7,8,9))
# print(calcate(1,2,3))
# print(calcate(1,2))
# print(calcate(1))


# # Create a function using **kwargs Print all student details.
# def pra(**kwargs):
#     for k , v in kwargs.items():
#         print(f"{k} = {v}")

# pra(name = "vedant", age = 21, course = "python")




# Create a function using both *args and **kwargs
def mojmasti(*args,**kwargs):
    for i in args:
        print(i)
    for k , v in kwargs.items():
        print(f"{k} = {v}")

        
mojmasti(1,2,3,4,5, name = "vedant", age = 21, course = "python")
       
