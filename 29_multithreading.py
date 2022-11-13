# Multithreading in Python

'''
Problem :
    For a given list of numbers print square and cube of every numbers-
    for example:
        input:[2,3,8,9]
        output:
            sq list : [4,9,64,81]
            cube list: [8,27,512,729]
'''

import time
import threading

def calc_sq(numbers):
    print("calculate square of numbers : ")
    for number in numbers:
        time.sleep(0.2)
        print("square: " + str(number*number) + "\n")

def calc_cube(numbers):
    print("calculate cube of numbers : ")
    for number in numbers:
        time.sleep(0.2)
        print("cube: " + str(number*number*number) + "\n")

numbers=[1,2,3,4]

# without multithreading
# t=time.time()
# calc_sq(numbers)
# calc_cube(numbers)
# print("it took "+str(time.time()-t)+"s to execute the program")

# with threading
t=time.time()

t1=threading.Thread(target=calc_sq, args=(numbers,))
t2=threading.Thread(target=calc_cube, args=(numbers,))

# starting thredas
t1.start()
t2.start()

# ending threds
t1.join()
t2.join()

print("it took "+str(time.time()-t)+"s to execute the program") # it will take less time , cpu won't take rest for 0.2 sec rather it will work on another function

'''
Note :
    Python is little special because there is something called a group global interpreter lock that prevents you from true befifits of multithreading.
    But in any case whenever you are waiting and when you are doing i/o bound operation, you can still use multithredaing.
    And if you want to do real CPU intensive work and you are not waiting for an i/o type operation, then you need to use multiprocessing.
'''