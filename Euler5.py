from math import *
prime = (2,3,5,7,11,13,17,19)

list = []
starts = 1
ends = 100000
check = "true"

for x in range(starts, ends):
    for divis in prime:
        if  (2520*x) % divis == 0:
            check = "true"
        else:
            check = "false"
            ##print "Break"
            break
    if check == "true":
        list.append(x)
        
        
print list[-1]*2520
     
num = 1
for y in prime:
    num = num * y

print num
