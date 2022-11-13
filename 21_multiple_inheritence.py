# Multiple inheritence in Python
'''
    Benifit of multiple inheritence is sometimes we have two different classes,
    you want to inherit properties and methods of those classes to a new class to reuse the code
    and add your own customization. Then you should use multiple inheritence.
'''
class Father():
    # def gardening(self):
    #     print("I enjoy gardening.")

    def skills(self):
        print("gardening, programming")

class Mother():
    # def cooking(self):
    #     print("I enjoy cooking.")

    def skills(self):
        print("art, cooking")

# Child inherits from Father and Mother
# We can inherit classes as many classes as we want
class Child(Father):
    def skills(self):
        print("sports.")
        Father.skills(self)
        Mother.skills(self)


c=Child()
c.skills()