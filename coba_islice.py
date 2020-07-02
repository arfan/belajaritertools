from itertools import islice

a = islice('ABCDEFG', 2)
b = islice('ABCDEFG', 2, 4)
c = islice('ABCDEFG', 2, None)
d = islice('ABCDEFG', 0, None, 2)

for i in a:
    print(i)
print()

for i in b:
    print(i)
print()

for i in c:
    print(i)
print()

for i in d:
    print(i)
print()
