from itertools import combinations_with_replacement

c = combinations_with_replacement([1,2,3,1], 2)

for i in c:
    print(i)



# (1, 1) (1, 1)
# (1, 2) (1, 2)
# (1, 3) (1, 3)
# (1, 4) (1, 1)
# (2, 2) (2, 2)
# (2, 3) (2, 3)
# (2, 4) (2, 1)
# (3, 3) (3, 3)
# (3, 4) (3, 1)
# (4, 4) (1, 1)
