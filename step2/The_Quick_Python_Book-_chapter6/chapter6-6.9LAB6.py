'''In processing raw text, it’s quite often necessary
to clean and normalize the text before doing anything else. If you want to
find the frequency of words in text, for example, you can make the job easier
if, before you start counting, you make sure that everything is lowercase (or
uppercase, if you prefer) and that all punctuation has been removed. You can
also make things easier by breaking the text into a series of words. In this lab,
the task is to read the first part of the first chapter of Moby Dick (found in the
book's source code), make sure that everything is one case, remove all punc-
tuation, and write the words one per line to a second file. Because I haven’t
yet covered reading and writing files, here’s the code for those operations:'''

import string
with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    s = string.punctuation
    cleaned_words = list()
    for line in infile:
# make all one case
# remove punctuation
# split into words
# write all words for line
        line = line.lower()
        line = line.translate({ord(i): None for i in s})
        line = line.split(' ')
        line = [i.strip('\n') for i in line if i.strip('\n') != '']
        cleaned_words.extend(line)
    cleaned_words= '\n'.join(cleaned_words)
    outfile.write(cleaned_words)