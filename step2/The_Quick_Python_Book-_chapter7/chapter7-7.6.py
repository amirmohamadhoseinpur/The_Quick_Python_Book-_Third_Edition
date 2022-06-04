'''Suppose that you’re writing a program that
works like a spreadsheet. How might you use a dictionary to store the con-
tents of a sheet? Write some sample code to both store a value and retrieve a
value in a particular cell. What might be some drawbacks to this approach?'''

spreadsheet = dict()
col = input('Enter column number:')
row = input('Enter Row number:')
val = input('Enter value:')

spreadsheet[(row,col)] = val

col = input('Enter column number:')
row = input('Enter Row number:')

print(spreadsheet[(row,col)])


# Enter the wrong number