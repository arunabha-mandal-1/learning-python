# Sharing data between two processes in Python
import multiprocessing

# result=[]

def calc_sq(numbers, result):
    for idx, number in enumerate(numbers):
        result[idx]=number*number

def dummy(number):
    number.value=20

if __name__=="__main__":
    numbers = [2,3,4,5]

    # shared memory
    result=multiprocessing.Array('i', 4)
    n=multiprocessing.Value('d', 99999)

    p1=multiprocessing.Process(target=calc_sq, args=(numbers,result))
    p2=multiprocessing.Process(target=dummy, args=(n,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()

    print("outside process : ", result[:]) # data exchanged
    print(n.value) # data exchanged

# using 'shared memory', we can share data between two processes
# child process is updating the value
#  and parent process are able to access the same value.