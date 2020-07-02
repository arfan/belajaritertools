from itertools import compress

c = compress([1,2,3,4,5,6], [[],[],1,0,1,1])

for i in c:
    print(i)
