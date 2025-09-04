def cube(n):
    return n**3
print(cube(3))


#----Even and odd
f = lambda n: 'Yes'if n%2==0 else 'No'
print(f(4))

#---Filter
lst = [2,4,6,8,9,13,15,17,19]
#--type casting is done for the filter object to a list
result = list(filter(lambda x: x%2==0, lst))
print(result)
for i in result: print(i)