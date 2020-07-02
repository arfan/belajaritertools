import operator
from itertools import accumulate

a = accumulate([10,2,3,4,5,6], max)

for i in a:
    print(i)
