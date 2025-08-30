print()
print("hello \n"*3)

a,b=10,20
print(a,b)
#---Use of seperator
print(a,b,sep="==")

#--Printing and formatting
name="John"
marks=90.5094
print(name,marks)
print("Name id ",name, "Marks are ",marks)
#---Formatting , %.2f is used to show only 2 places after decimal point
print("Name id %s and Marks are %.2f"%(name,marks))
#--Use of Format on the string, but the arithmetic values will not be restricted
print("Name is {} and Marks are {}".format(name,marks))


