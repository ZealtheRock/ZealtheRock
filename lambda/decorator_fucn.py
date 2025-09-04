#---Creation of Decorator
def decor(func):
    def inner():
        result = func()
        return result*2
    return inner
@decor      #---Same name as your decor function has
def num():
    return 5

#--Manual call/indicate
#resultfun = decor(num)
#---Direct call as we have annotated with @decor
print(num())