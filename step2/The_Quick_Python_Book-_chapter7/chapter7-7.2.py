'''Assume that you have a dictionary x =
{'a':1, 'b':2, 'c':3, 'd':4} and a dictionary y = {'a':6, 'e':5,
'f':6}. What would be the contents of x after the following snippets of code
have executed?:'''


x = {'a':1, 'b':2, 'c':3, 'd':4}
y = {'a':6, 'e':5, 'f':6}
del x['d']
z = x.setdefault('g', 7)
x.update(y)                # {'a': 6, 'b': 2, 'c': 3, 'g': 7, 'e': 5, 'f': 6}