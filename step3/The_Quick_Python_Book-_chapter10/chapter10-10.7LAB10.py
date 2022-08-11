'''Package the functions created at the end of chap-
ter 9 as a standalone module. Although you can include code to run the mod-
ule as the main program, the goal should be for the functions to be
completely usable from another script.'''

'''All functions are usable from another script'''

from chapter9LAB9 import *

text_list = readlines('moby_01.txt')

text_list = lower(text_list)

text_list = remove_punctuation(text_list)

words = lines_to_words(text_list)

words = remove_newline(words)

create_outfile(words, 'moby_01_clean.txt')

words = readwords('moby_01_clean.txt')

d = word_counter(words)

most = most_common(d)

least = least_common(d)

print(most)
print (least)