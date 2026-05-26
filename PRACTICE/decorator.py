
import exper as exp

def change(puuchi):
    def wrapper():
        print("01")
        puuchi()
    return wrapper

@change
def printer():
    print("employee")

printer()
@change
def trip():
   print("hima")

trip()


