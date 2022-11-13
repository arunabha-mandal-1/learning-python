# Functions in python
# Function is a block of code that performs a specific task

# You are given two lists of numbers and you need to find total of each of these list
# function example
def calculate_total(exp):
    total=0 # local
    for item in exp:
        total=total+item
    return total

# sum of two
def sum(a,b):
    return a+b

# multiply of two
def multiply(a,b=0.5):
    return a*b

def func(items):
    # Documentation string
    """
    description about the function, it's described here
    """
    total=0 # local
    for item in items:
        total+=item
    return item


tom_exp_list=[2100,3400,3500]
joe_exp_list=[200,500,700]

total=0; # global variable
# for item in tom_exp_list:
#     total=total+item
# print("Tom's total expenses :", total)

# total=0;
# for item in joe_exp_list:
#     total=total+item
# print("Joe's total expenses :", total)

# repeatative stuff above that's why we use function

toms_total=calculate_total(tom_exp_list)
joes_total=calculate_total(joe_exp_list)
print("Tom's total expenses :", toms_total)
print("Joe's total expenses :", joes_total)



### Arguments are of two types : 1. Positional arguments 2. Named Arguments

## Positional arguments
# n=sum(10,18) 
# print(n)

## Named arguments
# if you have long list of arguments and want to be specific about which argument has which value, the named args can be used
# n=sum(b=10,a=3)
# print(n)


# Default arguments
multiply_ans=multiply(10) # cuz a is provided  in the function
print(multiply_ans)

# print(total)