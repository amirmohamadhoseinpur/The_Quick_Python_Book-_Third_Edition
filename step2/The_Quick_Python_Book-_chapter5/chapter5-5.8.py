'''If you were to construct a set from the following list, how
many elements would the set have?: [1, 2, 5, 1, 0, 2, 3, 1, 1, (1,
2, 3)]'''

l = [1, 2, 5, 1, 0, 2, 3, 1, 1, (1, 2, 3)]
s = set(l)
print(len(s))       # will print 6