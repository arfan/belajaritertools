from itertools import product

p = product([1,2,3], ['a', 'b'])

for i in p:
    print(i)
    