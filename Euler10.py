from math import sqrt

def findPrime():
    MaxNumber = 2000001
    currentrange = range(2, MaxNumber)
    primenumbers = []
    j = 0
    prime = False
    sumprime = 0
    
    for j in currentrange :
        prime = True
        testTo = sqrt(j)
        for i in primenumbers :
            if i == 0 :
                break
            if j % i == 0 :
                #This is no longer prime
                prime = False
                break
            if i > testTo :
                prime = True
                break

        if prime : 
            primenumbers.append(j)
            sumprime+= j
                  
    print sumprime
    

import timeit
t1 =  timeit.time.clock()
findPrime()
t2 = timeit.time.clock()
print t2-t1


    