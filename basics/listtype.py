lst=[10,20,30,'Harsh Mani',72.5,76.6]
print(lst)
print(len(lst))
print(lst[0:5])
#----Dynamically Add and remove elements
print(lst.append(40))
print(lst)
print(lst.remove("Harsh Mani"))
print(lst)
#-----Use of del function to remove an element from provided index
del(lst[0])
print(lst)
#----Remove all the elements from a list
#print(lst.clear())
#print(lst)
#------get the Max and Min element in the list--#
print(max(lst))
print(min(lst))
#----sorting the list
print(lst.sort()) #--no parameter passed
print(lst)
print(lst.sort(reverse=True))
print(lst)

