'''Rewrite the word-count program from section
8.7 to make it shorter. You may want to look at the string and list operations
already discussed, as well as think about different ways to organize the code.
You may also want to make the program smarter so that only alphabetic
strings (not symbols or punctuation) count as words.'''
import string

s = string.punctuation
infile = open('word_count.tst')
txt = infile.read()
txt = txt.translate({ord(i): None for i in s})
char_count = len(txt)
print(char_count)
lines = txt.split("\n")
line_count = len(lines)
print(line_count)
words = txt.split()
word_count = len(words)
print(word_count)
print(txt)