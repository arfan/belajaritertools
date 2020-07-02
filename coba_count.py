from itertools import count

c = count(12, 3)

for i in range(1000):
    print(next(c))
