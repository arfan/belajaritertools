from itertools import tee

iterator1, iterator2 = tee([1, 2, 3, 4, 5], 2)

print(list(iterator1))
print(list(iterator1))
print(list(iterator2))