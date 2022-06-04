'''Which of the following will not be con-
verted to numbers, and why?'''

int('a1')                      # ValueError: invalid literal for int() with base 10: 'a1'
int('12G', 16)                 # ValueError: invalid literal for int() with base 16: '12G'
float("12345678901234567890")  # There is no problem in this item
int("12*2")                    # ValueError: invalid literal for int() with base 10: '12*2'