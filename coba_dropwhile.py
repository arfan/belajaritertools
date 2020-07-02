from itertools import dropwhile

def coba_predikat(x):
    return x < 4


d = dropwhile(coba_predikat, [1,2,3,4,1,2,3,4,6,4,1])

for i in d:
    print(i)