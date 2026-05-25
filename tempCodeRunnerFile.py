def pra(**kwargs):
    for k , v in kwargs.items():
        print(f"{k} = {v}")

pra(name = "vedant", age = 21, course = "python")