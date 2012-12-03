from math import *
number = 600851475143
sqrnumber = int((number)**.5)
totalsqaure = 1
primefactors = [1]


for j in range(1,sqrnumber):
    if number % j == 0 :
        primefactors.append(j)
        number = number/j

print primefactors
