'''Suppose that you have the following list: x = [[1, 2,
3], [4, 5, 6], [7, 8, 9]] What code could you use to get a copy y of
that list in which you could change the elements without the side effect of
changing the contents of x?'''

from copy import deepcopy

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = x[:]
y[0].append(66)
y[0] = [9, 10, 11]
print(y)                # will print   [[9, 10, 11], [4, 5, 6], [7, 8, 9]]
print(x)                # will print   [[1, 2, 3, 66], [4, 5, 6], [7, 8, 9]]

###########################################################################

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = deepcopy(x)
y[0].append(66)
print(x)                # will print [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(y)                # will print [[1, 2, 3, 66], [4, 5, 6], [7, 8, 9]]