from math import *
squarethensum = 0
sumthensquare = 0

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

for i in range(0,101):
    squarethensum = squarethensum + (i**2)
    sumthensquare = i + sumthensquare
    
ss = sumthensquare ** 2

print ss - squarethensum 

