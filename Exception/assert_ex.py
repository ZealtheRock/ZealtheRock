try:
    i=int(input("Enter an Even number: "))
    assert i%2==0, "You have not entered correct number"
except AssertionError as obj:
    print(obj)
print("After Assertion")