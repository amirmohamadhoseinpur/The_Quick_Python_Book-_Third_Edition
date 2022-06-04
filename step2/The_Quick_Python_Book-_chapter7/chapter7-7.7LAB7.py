'''In the previous lab, you took the text of the first chap-
ter of Moby Dick, normalized the case, removed punctuation, and wrote the
separated words to a file. In this lab, you read that file, use a dictionary to
count the number of times each word occurs, and then report the most com-
mon and least common words.'''

with open('moby_01_clean.txt') as f:
    txt = [i.strip('\n') for i in f.readlines()]
keys = list(set(txt))
d = dict()

for i in keys:
    d[i] = txt.count(i)
maximum = max(d.values())
minimum = min(d.values())

mx = list()
mn = list()
for i in keys:
    if d[i] == maximum:
        mx.append(i)
    elif d[i] == minimum:
        mn.append(i)
print('most common:'+repr(mx))
print('least common:'+repr(mn))