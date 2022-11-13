# Classes and Objects in Python(OOP)
'''
What is class?
    It falls under object-oriented programming paradigm.
    Class = property + method
    Object is specific instance of a class.
'''

class Human:
    def __init__(self, myName, myOccupation): # it going to initialize properties of the class object
        self.name=myName
        self.occupation=myOccupation
        '''
            myName, myOccupation => Arguments
            name, occupation => properties
        '''

    def do_work(self):
        if self.occupation=="tennis player":
            print(self.name, "plays tennis")
        elif self.occupation=="actor":
            print(self.name, "shoots a flim")
    
    def speaks(self):
        print(self.name, "says how are you?")

# tom is an instance of human class
tom=Human("tom cruise", "actor") # self is passed automatically
tom.do_work()
tom.speaks()

maria=Human("maria sharapove", "tennis player")
maria.do_work()
maria.speaks()

# tom, maria => object of class Human