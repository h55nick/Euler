from math import sqrt

def findPrime():
    MaxNumber = 2000000
    primenumbers = []
    j = 0
    number = 1
    prime = False
    sumprime = 0
    
    
    while j < MaxNumber  :
        number += 1
        prime = True
        testTo = sqrt(number)
        for i in primenumbers :
            if number % i == 0 :
                #This is no longer prime
                prime = False
                sumprime+= i
                break
            if i > testTo:
                break
           
                
        if prime : 
            primenumbers.append(number)
            j+= 1
                  
    print sumprime
    

import timeit
t1 =  timeit.time.clock()
findPrime()
t2 = timeit.time.clock()
print t2-t1


    