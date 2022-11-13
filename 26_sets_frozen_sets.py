# Sets and frozen sets in Python
# set is an unordered collection of unique sets
basket={"orange", "apple", "mango", "apple", "orange"} # remove duplicate elements automatically
# if i initialize it with {}, it wil be a dict
# i cannot use index cuz they are unordered

print(type(basket))
print(basket)

a=set()
print(type(a))
a.add(1)
a.add(2)
a.add(3)
a.add(3)
print(a)

# whenever we want to remove duplicate elements, we can use sets
numbers=[1,2,3,4,5,6,2,3,1]
unique_numbers=set(numbers)
unique_numbers.add(2)
unique_numbers.add(12)
print(unique_numbers)

# if we want our sets to be frozen so that we cannot change the content of the set
fs=frozenset(numbers)
print(fs)
# fs.add(5) # not allowed

x={'a', 'b', 'c'} # set
# x={"a", "b", "c"}
print('a' in x)
print('g' in x)

# list supports iterator
for i in x:
    print(i)

y={'a', 'd', 'g'}

print(x|y) # union
print(x&y) # intersection
print(x-y) # difference
print(x<y) # is x subset of y?
print(x.union(y)) # union