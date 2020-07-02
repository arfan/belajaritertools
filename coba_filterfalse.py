from itertools import filterfalse, chain

# False, 0, [], None
f = filterfalse(None, chain([None, 0, []], range(10)))

for i in f:
    print(i)