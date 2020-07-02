from itertools import chain

c = chain.from_iterable(['ABC', 'DEF', 'test'])

for i in c:
    print(i)