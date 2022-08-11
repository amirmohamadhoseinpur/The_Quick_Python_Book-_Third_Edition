'''How would you write a function
that could take any number of unnamed arguments and print their values out
in reverse order?
What do you need to do to create a procedure or void function—that is, a
function with no return value?
What happens if you capture the return value of a function with a variable?'''

def func1(*arg):
    arg = list(arg)
    arg.reverse()
    for i in arg:
        print(i)

def func2(*arg):
    arg = list(arg)
    arg.reverse()
    return arg

var1 = func1(1, 2, 3, 4, 5)     #var1 = None
var2 = func2(9, 8, 3, 2, 5)     #var2 = [5, 2, 3, 8, 9]