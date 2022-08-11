'''Suppose that you have a module called new_math
that contains a function called new_divide. What are the ways that you
might import and then use that function? What are the pros and cons of each
method?
QUICK CHECK: MODULES
Suppose that the new_math module contains a function call
_helper_math(). How will the underscore character affect the way that
_helper_math() is imported?'''

import new_math

new_math.new_divide()
new_math._helper_math()      # no error

##################################################################

from new_math import new_divide
from new_math import _helper_math()

'''If two modules
both define a name, and you import both modules using this form of importing,
you’ll end up with a name clash, and the name from the second module will replace
the name from the first.'''

new_divide()
_helper_math()               # no error

##################################################################

from new_math import *

'''If two modules
both define a name, and you import both modules using this form of importing,
you’ll end up with a name clash, and the name from the second module will replace
the name from the first.'''

new_divide()
_helper_math()               # NameError will occur
##################################################################