# BUBBLE SORT

from array import *

a = array('i', [118, 4, 53, 74, 88, 35, 23, 66, 786, 4234, 23, 65645, 22, 1])
x = 0

for z in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i] = a[i]+a[i+1]
            a[i+1] = a[i]-a[i+1]
            a[i] = a[i]-a[i+1]


for i in range(len(a)):
    print(a[i], end=' ')
