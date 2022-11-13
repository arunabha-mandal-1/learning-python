# Multiprocessing Lock in Python

import time
import multiprocessing

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)

        # -----critical section-------> the section of code is accessing the shared resource which you want to protect, that part is called critical section
        lock.acquire()
        balance.value=balance.value+1
        lock.release()
        # -----critical section-------

def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)

        lock.acquire()
        balance.value=balance.value-1
        lock.release()

if __name__=="__main__":
    balance=multiprocessing.Value('i', 200) # shared memory resource

    # locking
    lock=multiprocessing.Lock()

    d=multiprocessing.Process(target=deposit, args=(balance,lock))
    w=multiprocessing.Process(target=withdraw, args=(balance,lock))
    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)


# Why lock is needed in our real life?
# In our day-today life, there are things which cannot be accessed by the two people at the same time.
# e.g. bathroom=>shared resource with lock

# Whenever two processes/threads are trying to share resources(memory,files,databases), it can create problem.
# You need to protect that access with a lock

