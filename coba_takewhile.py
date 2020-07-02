from itertools import takewhile

t = takewhile(lambda x: x<5, [1,4,6,4,1])

for i in t:
    print(i)
