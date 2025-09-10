try:
    f=open("Demo","w")
    a,b=[int(x)for x in input("Enter two numbers :").split()]
    c = a/b
    f.write(f"Writing %d into :" %c)
except ZeroDivisionError:
     print("You can't divide by zero")
     print("Enter a non-zero number")
finally:
    f.close()
    print("File closed")
print("After division by zero case handled")
