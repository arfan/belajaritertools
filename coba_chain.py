from itertools import repeat, chain

a = repeat(2, 5)
b = repeat(3,10)
d = range(10)

c = chain(a, b, d)

for i in c:
    print(i)

for i in chain('abc', 'def'):
    print(i)

