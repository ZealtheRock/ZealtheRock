dict1={1:'john',2:'doe',3:'bill',4:'nero'}
print(dict1)  #---Print the dictionary

#---Print the items in dictionary, as in paired (key:value) view
print(dict1.items())

#--- Fetching/Accessing and iterating with Keys of dictionary
dict1_key = dict1.keys()
for k in dict1_key:
    print(k)
#----Fetching or Accessing values of Dictionary
dict1_values=dict1.values()
for v in dict1_values:
    print(v)
#--Accessing specific values by providing the key,not index
print(dict1[2])

#---Deleting an Element from a Dictionary
del dict1[2]
print(dict1.items())
