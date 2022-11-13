'''
    Every process has its own address space(virtual memory).
    Thus program variables are not shared between two processes.
    You need to use interprocess communication(IPC) techniques if you want to share data between two processes.
'''

import multiprocessing

sq_result=[]
def calc_sq(numbers):
    global sq_result
    for number in numbers:
        print("square " + str(number*number))
        sq_result.append(number*number)
    print("within process result : " + str(sq_result))

if __name__=="__main__":
    arr=[2,3,8,9]

    p1=multiprocessing.Process(target=calc_sq, args=(arr,))

    # start
    p1.start()
    # wait untill the execution of the processes is over
    p1.join()

    print("result : " + str(sq_result)) # will print an empty list cuz the process creates a copy of sq_result in the process
    print("Done!")