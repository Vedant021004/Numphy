def hum(vedrid , **kwargs):
    print(vedrid)
    for k, c in kwargs.items():
        print(f"{k} = {c}")

hum("vedant", name ="vedant", rollno = 36, age = 21, course = "python")