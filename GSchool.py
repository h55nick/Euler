from math import sqrt

def findPrime():
    MaxNumber = 10001
    primenumbers = []
    j = 0
    number = 1
    prime = False
    
    
    while j < MaxNumber  :
        number += 1
        prime = True
        testTo = sqrt(number)
        for i in primenumbers :
            if number % i == 0 :
                #This is no longer prime
                prime = False
                break
            if i > testTo:
                break
           
                
        if prime : 
            primenumbers.append(number)
            j+= 1
            
            
    print primenumbers[-1]

import timeit
t1 =  timeit.time.clock()
findPrime()
t2 = timeit.time.clock()
print t2-t1


    