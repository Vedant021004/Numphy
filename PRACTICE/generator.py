# yeild
def func(result):
    for i in range(result):
        result = result*2
        yield result
        
print(func(5))