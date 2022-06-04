'''What would be a quick way to change all
punctuation in a string to spaces?'''

import string
s = 'any string ()$with . '
for i in string.punctuation:
    s = s.replace(i,' ')
print(s)