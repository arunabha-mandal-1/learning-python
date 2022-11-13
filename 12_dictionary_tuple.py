# Dictionaries and tuples in Python
# dictionary allows you to store key, value pairs
# also knowns as maps, hashtables, associative arrays
# e.g telephone directory

d={'arunabha':1234567890, 'tom':7896523685, 'jack':4563268596}
print(d['tom'])
# print(d['tomi']) # error

# adding new 
# order does not matter cuz it we use dictionary values using keys
d['kartik']=5632415685 # 
# d["tom"]=5236547852 # updated
d['jill']=8541237852

# delete
del d['arunabha']
print(d)

# accessing all the dicectory values
# for key in d:
#     print("key:", key, "value", d[key])

# another way
for k,v in d.items():
    print("key:", k, "value", v)


# is a key is present in the dictionary
print("tom" in d)
print("tomi" in d)

# delete all the entries from the dictionary dictionaries
d.clear()
print(d)




# Tuples : A list of values grouped together
point=(5,9) # geometric point
print(point[0])
print(point[1])

# difference of lists and tuples
# tuple : all the values have different meaning(heterogeneous)
# list : all the values have similar meaning(homogeneous)

# here we are storing x and y co-ordinates => different meaning => use tuple
# but if we have to use all x values, we should use list

# tuples are immutable
# lists are mutable
mylist=["arunabha", "alex", "ankit"]
print(mylist)
mylist[0]="kittu"
print(mylist)
# point[0]=56 error

# tuple e.g. : geometric point, address
# list e.g. : expense list, list of names