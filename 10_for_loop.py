# For loops in python
# For loops are used whenever we want to do a range of things


expenses=[2340, 1000, 1563, 2150, 6385]
total_expenses=expenses[0]+expenses[1]+expenses[2]+expenses[3]+expenses[4]
print("Total expenses : ", total_expenses)
# We can sum one by one

# Using for loop
total=0
for item in expenses:
    total+=item
print("Total expenses : ", total)

# range function(start, stop+1)
# for i in range(1,11): # start is included, stop is excluded
#     print(i)


# for i in range(20,30,3): # third arg is step
    # print(i)

# for i in range(5): # starts from 0 if start index is not provided
    # print("i")

# len function
# total2=0
# for i in range(len(expenses)): # equivalent to 'range(5)'
#     print("Month:", i+1, "Expense: ", expenses[i])
#     total2=total2+expenses[i]

# print("Total :", total2)

# break
key_location="bathroom"
locations=["garage", "living room", "chair", "closet"]
for location in locations:
    if location==key_location:
        print("Key is found in", key_location)
        break
else: # else statement againest for loop
    print("Key is not found.")

# continue
# print square of numbers between 1 to 5 except even numbers
for i in range(1,6):
    if i%2==0:
        continue
    print(i*i)

# while statements
i=1
while i<=5:
    print(i)
    i=i+1


