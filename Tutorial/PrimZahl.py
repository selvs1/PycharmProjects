import time
import math

def primTest(biggestPrim, delta):
    for zahl in range(biggestPrim, biggestPrim+delta):
        #n=int(input())
        n = zahl
        start_time=time.process_time()
        count=0
        n1=int(math.sqrt(n))
        for i in range (2,n1):
            if (n%i==0):
                count=count+1
                break
        if count>0:
            continue
        else:
            print("PRIME", (n))
        print(time.process_time()-start_time,"seconds")


primTest(67280421310721, 1)




