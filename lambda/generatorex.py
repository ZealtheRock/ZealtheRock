def customgenerator(x,y):
    while x<y:
        yield x
        x+=1
result = customgenerator(10,45)  #----Last range will be excluded
for item in result:
    print(item)
