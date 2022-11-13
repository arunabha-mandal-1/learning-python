# Strings in Python


myText="ice cream"
print(myText[0]) # accessing string characters

# myText[0]='l' # err cuz strings are immutable in Python
# we can store anything in this same variable but we can change this string partially

print(myText[0:3]) # first index is inclusive and second index is exclusive
print(myText[4:]) # ends at last index
print(myText[:3]) # starts from zero

# both are valid
text1="Arunabha"
text2='Mandal'
print(text1, text2)

# when there is single quote in the string, use double quote and vice versa

# store multi line strings
my_address='''Arunabha Mandal
Basudev Mandal
Unai
Kalupur
Bongaon
North 24 Parganas
743235''' # internally it uses \n->new line
print(my_address)

# Concatenate two strings
s1="Hello"
s2="World"
s3=s1+" "+s2
print(s3)

# Concatenate string and number
# first convert the number to a string and then concatenate
text3="My age is "
age=19
# age_text=text3+n # wrong
age_text=text3+str(age) # right
print(age_text)