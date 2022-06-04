'''MODIFYING LISTS Suppose that you have a list 10 items long. How
might you move the last three items from the end of the list to the beginning,
keeping them in the same order?'''

a = [1,2,3,4,5,6,7,8]

def func(var):
    new_var = var[-3:]
    new_var.extend(var[0:-3])
    return new_var
print(func(a))      # The result is [6, 7, 8, 1, 2, 3, 4, 5]