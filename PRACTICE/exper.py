def change(puuchi):
    def wrapper():
        print("01")
        puuchi()
    return wrapper