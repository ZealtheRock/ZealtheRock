#-------defining a set, wont allow the duplicates
s={10,20,'demo',10,20}
print(type(s))
print(s)
#----Update a set

s.update([88,99])  #-- This is how set can be updated, but no order guarantee
print(s)

#-- Remove an element
print(s.remove(20))
print(s)

#----Set does not support, below operations
#-Indexing
#print(s[0]) #---try to get the element at index 0

#--Slicing
#print(s[0:5])

#--Repeatition
#print(s*3)

#---Frozen set-------
f=frozenset(s)
print(f)
#---It does not support update or delete operations