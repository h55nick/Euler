from math import *

FibSeq = [0,1,1]
maxfib = 4000000 


nfib = 0
efib = []
tefib = 0

while nfib < maxfib :
    nfib = FibSeq[-1]+FibSeq[-2]
    FibSeq.append(nfib)
    if nfib % 2 == 0:
        efib.append(nfib)
        tefib+=nfib
        

print FibSeq
print efib
print tefib

