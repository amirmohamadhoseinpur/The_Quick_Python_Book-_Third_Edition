'''What would be in the variable x
after the following snippets of code have executed?'''

x = "%.2f" % 1.1111                # 1.11
x = "%(a).2f" % {'a':1.1111}       # 1.11
x = "%(a).08f" % {'a':1.1111}      # 1.11110000