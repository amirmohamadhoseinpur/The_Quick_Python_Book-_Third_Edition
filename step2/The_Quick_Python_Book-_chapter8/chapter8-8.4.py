'''What list comprehension would you use to pro-
cess the list x so that all negative values are removed?

Create a generator that returns only odd numbers from 1 to 100. (Hint: A
number is odd if there is a remainder if divided by 2; use % 2 to get the
remainder of division by 2.)
Write the code to create a dictionary of the numbers and their cubes from 11
through 15.'''

x = [1, 3, 5, 0, -1, 3, -2]
x = [i for i in x if i >= 0]

gen = (i for i in range(1,101) if i%2==1)
d = {i:i**3 for i in range(11,16)}
