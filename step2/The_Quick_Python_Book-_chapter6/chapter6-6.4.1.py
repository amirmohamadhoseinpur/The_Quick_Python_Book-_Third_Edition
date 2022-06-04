'''How could you use split and join to change
all the whitespace in string x to dashes, such as changing "this is a test"
to "this-is-a-test"?'''

s = "this is a test"
l = s.split()
s = '-'.join(l)
print(s)        # The result is this-is-a-test