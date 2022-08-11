'''TRY THIS: GLOBAL VS. LOCAL VARIABLES Assuming that x = 5, what will be the
value of x after funct_1() below executes? After funct_2() executes?'''

def funct_1():
    x = 3
def funct_2():
    global x
    x = 2
funct_1()        # x will be 5
funct_2()        # x will be 2