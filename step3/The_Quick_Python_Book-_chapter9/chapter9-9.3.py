'''What would be the result of
changing a list or dictionary that was passed into a function as a parameter
value? Which operations would be likely to create changes that would be visi-
ble outside the function? What steps might you take to minimize that risk?'''

def func(arg):
    '''Any changes other than Reassigning would be visible outside the function'''
    from copy import deepcopy
    new = deepcopy(arg)       #To minimize that risk