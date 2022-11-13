# Multiprocessing pool in Python
from multiprocessing import Pool
import time

# def f(number):
#     return number*number

def fsum(n):
    sum=0
    for x in range(10000):
        sum=sum+x
    return sum

if __name__=="__main__":
    # array=[1, 2, 3, 4, 5]

    # p1=Pool()
    # result1=p1.map(f,array) # goona divide the work all the work equally between all available cores
    # p1.close()
    # p1.join()


    # visually we don't see any change but internally it has divided the work
    # even if we do performance measure, we can't see anything cuz the task is very simple
    
    # print(result1)

    # so we are doing this
    # doing sum cpu more cpu intensive work
    t1=time.time()
    p2=Pool()
    result2=p2.map(fsum, range(10000))
    p2.close()
    p2.join()
    print("pool took", time.time()-t1, "sec")

    t2=time.time()
    result3=[]
    for x in range(10000):
        result3.append(fsum(10000))
    print("serial processing took", time.time()-t2, "sec")
    # in case of small program with less iterations in fsum, serial processing is working much better
    # but when iterations are getting larger, pool is working much better

# in case we want to divide processes
# p=Pool(processes=3)


'''
Nowadays most of the computers have multiple cores in CPU.
When we run a simple program, it's ok and computer uses one core.
But when we run CPU intensive program, computer uses multiple cores. 
CPU divide the input among multiple cores and then aggregate the results back.
The first step is called map and the second step is called reduce.
'''