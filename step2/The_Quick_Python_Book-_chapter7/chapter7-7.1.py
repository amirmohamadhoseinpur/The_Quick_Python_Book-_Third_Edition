'''Write the code to ask the user for three
names and three ages. After the names and ages are entered, ask the user for
one of the names, and print the correct age.'''

d = dict()
name = input('Enter a name:')
age = input('Enter the age for the name:')
d[name] = age
name = input('Enter a name:')
age = input('Enter the age for the name:')
d[name] = age
name = input('Enter a name:')
age = input('Enter the age for the name:')
d[name] = age

name = input('Enter a name:')
print(d[name])