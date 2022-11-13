# Lists in Python


items=["bread", "pasta", "fruits", "vegetables"]
print(items)
print(items[0])

# modify
# items[0]="chips"
# print(items)

# access a range of elements
print(items[0:2]) # first index is included and second index is excluded
print(items[-1]) # first from the last

# append
# items.append("butter") # at the end
# print(items)

# insert at a particular location
items.insert(1, "butter")
print(items)

# join two lists
food_items=items
bathroom_items=["shampoo", "soap"]
all_items=food_items+bathroom_items
print(all_items)

# all_items+"soda" # wrong

# list
print(len(all_items))

# find if a element is present
print("bread" in all_items) # true
print("soda" in all_items) # false