from  functools import reduce

lst = [2,5,6,8,9]

result = reduce(lambda x,y:x+y,lst)
print(result)