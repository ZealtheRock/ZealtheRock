#-----Defining a tuple, if a single element is there then still a comma is needed. ex-a=(10,)
tpl=(10,20,30,40,10)
print(tpl)
#----It immutable, can not be modified once declared
#******tpl[2]=32, the tuple is immutable
print(tpl[2])
print(type(tpl))
#---repeating the elements of tuple
print(tpl*3)
#----Count the occurrence of an element in tuple
print(tpl.count(10))
#------Find the index of the a given element in tuple
print(tpl.index(10))
#--It will return the index of first occurrence of the element
