from itertools import zip_longest

a = zip_longest([1,2,3], ['a', 'b', 'c', 'd'], fillvalue=0)


for i in a:
    print(i)