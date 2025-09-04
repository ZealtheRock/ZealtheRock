def half(fun):
    def inner():
        n = fun()
        return n/2
    return inner

def square(fun):
    def inner():
        n = fun()
        return n * n
    return inner


def cube(fun):
    def inner():
        n = fun()
        return n ** 3
    return inner
#--Decorator Chaining

@cube
@square
@half
def num():
    return 5

print(num())

