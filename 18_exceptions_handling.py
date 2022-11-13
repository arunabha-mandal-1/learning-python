# Exceptions handling in Python
# Exceptions are errors detected at the time of program execution
# Tracebacks are usually exceptions
# If exceptions happens, programs stop on that particular line and will terminate

# few examples
'''
1. division by zero
2. 'abc'+2 => string + int
'''

x=input("Enter number1 : ") # by default string, will have to convert it first to number
y=input("Enter number2 : ")

# here's how to handle exception -> try catch
# using try-catch we can move forward even if exceptions happen without carshing
try:
    z=(x)/int(y)
# except Exception as e: # generic way of handling things
except ZeroDivisionError as e: # when we except a specific situation
    print("Division by zero exception.")
    z=None
# except Exception as e:
except TypeError as e:
    # print("Exception type :", type(e).__name__)
    print("TypeError exception.")
    z=None

print("Division is ", z)


'''
Accident-detour exception:

try:
    while road_is_clear():
        drive()
except Accident as e:
    take_detour()
'''