'''If you have a list x, write the code to safely remove
an item if—and only if—that value is in the list.
Modify that code to remove the element only if the item occurs in the list
more than once.'''

a = [1,2,3,4,5,6,7]
j = 1
#################################################################
if j in a:
    a.remove(j)

#################################################################
a = [1,2,3,4,5,6,7]
j = 1

#################################################################
if a.count(j) > 1:
        a.remove(j)