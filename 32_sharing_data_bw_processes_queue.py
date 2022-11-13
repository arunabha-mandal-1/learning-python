# Sharing Data Between Processes Using Multiprocessing Queue, queue is basically shared memory
# different different processes use their different memory spaces
import multiprocessing

# queue module is different from multiprocessing queue
# multiprocessing queue lives in shared memory and queue module lives in in-process memory
# multiprocessing queue is used to share data between processes and queue module is used to share data between threads

result=[]

# child process
def calc_square(numbers,q):
    for number in numbers:
        q.put(number*number)

# parent process
if __name__=="__main__":
    numbers=[3,5, 6]
    q=multiprocessing.Queue()
    p1=multiprocessing.Process(target=calc_square, args=(numbers,q))
    p1.start()
    p1.join()

    while q.empty() is False:
        print(q.get())