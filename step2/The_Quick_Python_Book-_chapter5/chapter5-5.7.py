'''Explain why the following operations aren’t legal for
the tuple x = (1, 2, 3, 4):
x.append(1)
x[1] = "hello"
del x[2]
If you had a tuple x = (3, 1, 4, 2), how might you end up with x sorted?'''


# Explain why the following operations aren’t legal for the tuple x = (1, 2, 3, 4):
# Because tuples are immutable.

# If you had a tuple x = (3, 1, 4, 2), how might you end up with x sorted?

x = (3, 1, 4, 2)
x = list(x)
x.sort()
x = tuple(x)