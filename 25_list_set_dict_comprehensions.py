# List set Dict comprehensions
# List comprehension provides a way to transform one list into another
# same applies to set and dict as well

numbers=[1,2,3,4,5,6,7,8]

# simple method
even1=[]
for i in numbers:
    if i%2==0:
        even1.append(i)
print(even1)

# list comprehension method
even2=[i for i in numbers if i%2==0]
print(even2)

sq_numbers=[i*i for i in numbers]
print(sq_numbers)

'''
    Set is unordered collection of unique items.
    The basic difference set and list is that set is unordered and it does not allow you to contain duplicate items
    Explore this more...
'''
s=set([1,2,3,4,5,2,3]) # will clean 2,3
print(s)
even3={i for i in s if i%2==0}
print(even3)

s1=set(["arunabha", "kittu", "mandal", "kittu"])
print(s1) # unordered

# dictionary comprehension
cities=["mumbai", "nyc", "paris"]
countries=["india", "usa", "france"]
z=zip(cities, countries)
print(z)
for a in z:
    print(a)

z=zip(cities, countries)
d={city:country for city, country in zip(cities, countries)} # key:value
# d={city:country for city, country in z} # key:value
print(d)

