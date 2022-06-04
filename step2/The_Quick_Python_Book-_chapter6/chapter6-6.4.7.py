'''Suppose that you have a list of strings in which
some (but not necessarily all) of the strings begin and end with the double
quote character:
x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']
What code would you use on each element to remove just the double quotes?
What code could you use to find the position of the last p in Mississippi?
When you’ve found that position, what code would you use to remove just
that letter?'''

x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']
for i in x:
    y = i.replace('"','')
    print(y)

##########################################################################

s = 'Mississippi'
n = s.rfind('p')
print(n)

###########################################################################

l = list(s)
l[9] = ''
s = ''.join(l)
print(s)