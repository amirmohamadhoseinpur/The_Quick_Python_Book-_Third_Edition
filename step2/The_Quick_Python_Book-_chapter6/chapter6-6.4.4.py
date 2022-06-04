'''If you wanted to check whether a line ends
with the string "rejected", what string method would you use? Would there
be any other ways to get the same result?'''


s = 'What you wnat rejected'
s.endswith('rejected')

s[-8:] == 'rejected'      # The same result