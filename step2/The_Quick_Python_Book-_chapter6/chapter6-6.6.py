'''What will be in x when the following
snippets of code are executed?:'''
x = "{1:{0}}".format(3, 4)                          # x = '  4'
x = "{0:$>5}".format(3)                             # x = '$$$$3'
x = "{a:{b}}".format(a=1, b=5)                      # x = '    1'
x = "{a:{b}}:{0:$>5}".format(3, 4, a=1, b=5, c=10)  # x = '    1:$$$$3'