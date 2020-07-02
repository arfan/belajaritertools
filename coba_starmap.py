import operator
from itertools import starmap

s = starmap(operator.mul, [(2,5), (3,2), (10,3)])

for i in s:
    print(i)