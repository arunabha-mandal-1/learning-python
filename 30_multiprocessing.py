# Multiprocessing in Python

import time
import multiprocessing

'''
Create two processes:
    1. First is to calculate square of all numbers
    2. Second one is to calculate cube of numbers
'''

square_result=[]
cube_result=[]

def calc_sq(numbers):
    for number in numbers:
        # time.sleep(5) # just to see in task manager
        print("square " + str(number*number))

def calc_cube(numbers):
    for number in numbers:
        # time.sleep(5)
        print("cube " + str(number*number*number))


if __name__=="__main__":
    arr=[2,3,8,9]

    p1=multiprocessing.Process(target=calc_sq, args=(arr,))
    p2=multiprocessing.Process(target=calc_cube, args=(arr,))

    # start
    p1.start()
    p2.start()

    # wait untill the execution of the processes is over
    p1.join()
    p2.join()

    print("Done!")

# three process => one for 'main' and another two for two functions
# when we do multithreading, we don't see processes in the task manager the way we've seen

# printing in console might be vary from one time to another time