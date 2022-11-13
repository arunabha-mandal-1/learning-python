# If statements in Python
# num = input("Enter a number : ")
# num=int(num) # Converting to integer
# if num%2==0:
#     print("Number is even.")
# else:
#     print("Number is odd.")

# Operators


# print(4==4) # true
# print(4!=5) # false
# print(4!=4) # false
# print(2>1) # true
# .....and others conditional like other programming languages
# print(3>2 and 4>1) # true
# print(2>3 and 4>1) # false
# print(2>3 or 4>1) # true
# print(not True) # false
# print(not 4==4) # false

# which cuisine is that dish
indian=["samosa","daal","naan"]
chinese=["egg roll","pot sticker","fried rice"]
italian=["pizza","pasta","risotto"]

dish=input("Enter a dish name : ");
if dish in indian: # checking the whole list
    print("Indian dish.")
elif dish in chinese:
    print("Chinese dish.")
elif dish in italian:
    print("Italian dish.")
else:
    print("I do not know.")
