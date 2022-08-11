'''What would you need to modify in the
previous code for the function four()to make it work for any number? What
would you need to add to allow the starting point to also be set?'''

def four(num):
    x = 0
    while x < num:
        print("in generator, x =", x)
        yield x
        x += 1

def four(start, num):
    x = start
    while x < num:
        print("in generator, x =", x)
        yield x
        x += 1