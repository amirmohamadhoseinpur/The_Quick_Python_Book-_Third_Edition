'''LAB 9: USEFUL FUNCTIONS Looking back at the labs in chapters 6 and 7, refac-
tor that code into functions for cleaning and processing the data. The goal
should be that most of the logic is moved into functions. Use your own judg-
ment as to the types of functions and parameters, but keep in mind that func-
tions should do just one thing, and they shouldn’t have any side effects that
carry over outside the function.'''



def readlines(filename):
    lines = list()
    with open(filename) as infile:
        lines = list()
        for i in infile:
            lines.append(i)
    return lines

def lower(text_list):
    return [i.lower() for i in text_list]

def remove_punctuation(text_list):
    import string
    s = string.punctuation
    return [line.translate({ord(i): None for i in s}) for line in text_list]

def lines_to_words(text_list):
    new_text_list = list()
    for i in text_list:
        line = i.split(' ')
        new_text_list.extend(line)
    return new_text_list

def remove_newline(text_list):
    return [i.strip('\n') for i in text_list if i.strip('\n') != '']

def create_outfile(text_list, outfile):
    text = '\n'.join(text_list)
    with open(outfile, 'w') as f:
        f.write(text)

text_list = readlines('moby_01.txt')

text_list = lower(text_list)

text_list = remove_punctuation(text_list)

words = lines_to_words(text_list)

words = remove_newline(words)

create_outfile(words, 'moby_01_clean.txt')
###################################################################################

def readwords(filename):
    with open(filename) as infile:
        words = infile.readlines()
    return words

def word_counter(words):
    d = dict()
    keys = set(words)
    for i in keys:
        d[i] = words.count(i)
    return d

def most_common(d):
    maximum = max(d.values())
    words = [i for i in d if d[i] == maximum]
    return words

def least_common(d):
    minimum = min(d.values())
    words = [i for i in d if d[i] == minimum]
    return words

words = readwords('moby_01_clean.txt')

d = word_counter(words)

most = most_common(d)

least = least_common(d)
