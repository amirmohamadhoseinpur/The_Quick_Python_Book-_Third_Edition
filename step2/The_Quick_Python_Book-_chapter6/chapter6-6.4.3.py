'''If the string x equals "(name, date),\n", which of
the following would return a string containing "name, date"?'''

x = "(name, date),\n"
x.rstrip("),")
x.strip("),\n")
x.strip("\n)(,")    # The answer