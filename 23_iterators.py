# Iterators
# Key topics -> 1. What is iterators? 2. Iterator implementation using class

a=["hey", "bro", "how", "are", "you?"]
# for i in a:
#     print(i)

# but how does this work internally? it uses a built-in method 'iter'
# print(dir(a))
# itr=iter(a)
# print(dir(itr))
# print(itr)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# for loop internally calling next method on itr object

# iterating through a list
# for element in [1,2,3]:
#     print(element)
# # iterating through a tuple
# for element in (7,8,9):
#     print(element)
# # iterating through a dict
# for key in {'one':1, 'two':2}:
#     print(key)
# # iterating through a string
# for char in "abc":
#     print(char)
# for line in open("23_myfile.txt"):
#     print(line, end='')

## iterating in a reverse order
# itr=reversed(a)
# print(next(itr))
# print(next(itr))

class RemoteControl():
    def __init__(self):
        self.channels=["HBO", "cnn", "abc", "espn"]
        self.index=-1

    # in order to define itrerator, you have to define this built-in method __iter__
    def __iter__(self):
        return self

    def __next__(self):
        self.index+=1
        if self.index==len(self.channels):
            raise StopIteration
        return self.channels[self.index]

r=RemoteControl()
itr=iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
# print(next(itr))
# print(next(itr))