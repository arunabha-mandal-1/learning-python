# Inheritence in Python(OOP)
# Car and motor cycle are classes that *inherit* from Vehicle class

class Vehicle:
    def general_usage(self):
        print("general use: transportation")

class Car(Vehicle): # inheriting class from another class
    def __init__(self):
        print("I am car.")
        self.wheels=4
        self.has_roof=True
    
    def specific_usage(self):
        self.general_usage()
        print("specific use: commute to work, vacation with family")
    
class MotorCycle(Vehicle):
    def __init__(self):
        print("I am motor cycle")
        self.wheels=2
        self.has_roof=False

    def specific_usage(self):
        self.general_usage()
        print("specific use: road trip, racing")


c=Car()
# c.general_usage() # cuz i have inherited this method from Vehicle class
# c.specific_usage()

m=MotorCycle()
# m.general_usage() # calling from specific_usage() method
# m.specific_usage()


'''
    you can call a method or a property from your parent class using the object of your derived class
'''

'''
Benifits of inheritence:
    1. Code Reuse : We can reuse code from our parent class.
    2. Extensiblity : We can one class to make another class.
    3. Readability : Nice structure, readable, simple.
'''

# isinstance and issubclass methods
print(isinstance(c,Car))
print(isinstance(c,MotorCycle))

print(issubclass(Car, Vehicle))
print(issubclass(Car, MotorCycle)) # car is more like sibling of motorcycle