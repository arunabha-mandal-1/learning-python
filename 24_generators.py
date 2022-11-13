# Generators in Python
# generator is a simple way of creating iterator
# it is useful when we have a lot of values and we don't want to return them in one shot
def remote_control_next():
    yield "cnn"
    yield "espn"
    yield "bbc"
    yield "discovery"

# method 1
itr=remote_control_next()
print(next(itr), end=" ")
print(next(itr), end=" \n")
print("-------")


# method 2
for channel in remote_control_next():
    print(channel, end=" ")
print("\n")

# Produce fibonacci sequence using generator
def fib():
    a,b=0,1
    while True:
        yield a # holds the previous value
        a,b=b,a+b

for f in fib():
    if (f>100):
        break
    print(f, end=" ")

''' generators are better over class based iterator,
        1. u don't need to define iter() and next() method
        2. u don't need to raise StopIteration exception
'''
