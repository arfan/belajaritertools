from itertools import repeat

r = repeat(10, 5)

for i in r:
    print(i)

print(list(map(pow, range(100), repeat(2))))