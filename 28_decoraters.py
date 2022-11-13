# Decorators in Python
import time

# def calc_square(numbers):
#     start=time.time()
#     result=[]
#     for number in numbers:
#         result.append(number*number)
#     end=time.time()
#     print("calc_square took " + str((end-start)*1000) + " mil sec")
#     return result

# def calc_cube(numbers):
#     start=time.time()
#     result=[]
#     for number in numbers:
#         result.append(number*number*number)
#     end=time.time()
#     print("calc_cube took " + str((end-start)*1000) + " mil sec")
#     return result

# suppose we have a software project that contains 2000 function, we have to calculate time taken by 2000 functions in order to measure performance of that software
# plus time logic is getting mixed up with the function logic and it also looks messy
# there is a better way of doing this and that is "decorater"

# decorater allows you to wrap your function into another function

# first define wrapper function
# functions are first class objects in Python
# what it means is that they can be treated just like any other variable and you can pass them as argument to another function or even return them as a return value
def time_it(func):
    # python allows to write nested function
    def wrapper(*args, **kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        end=time.time()
        print(func.__name__+" took "+str((end-start)*1000)+" mil sec.")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result=[]
    for number in numbers:
        result.append(number*number*number)
    return result

array=range(1,100000)
out_sq=calc_square(array)
out_cube=calc_cube(array)

# *args(variable number of positional arguments) receives arguments as an array
# **kwargs(variable number of keyword arguments) receives arguments as a dictionary