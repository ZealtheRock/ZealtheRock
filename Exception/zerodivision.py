import logging

logging.basicConfig(filename="myfile.log", level=logging.DEBUG)

print("Enter two numbers:")
a = int(input())
b = int(input())
try:
    c= (a/b)
    logging.info("Division by zero is: " + str(c))
except ZeroDivisionError:
    print("You can't divide by zero")

