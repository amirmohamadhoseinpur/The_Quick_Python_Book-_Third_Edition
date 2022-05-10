a = 'amir'
b = 4
e = 2.7
c = 4 + 4j

m = a * b   # m = 'amiramiramiramir'
m = a * e   # TypeError will accour
m = a * c   # TypeError will accour

##############################################################
from math import *

y = atan(1)       # y = 0.785398 return the arc tangent
y = factorial(3)  # y = 6      y=3!
y = pow(3,4)      # y = 81     y=3**4

##############################################################

from cmath import *

y = acos(1+1j)   # y = (0.9045568943023814-1.0612750619050357j)    Return the arc cosine of z
y = log(100)     # y = (4.605170185988092+0j)                      the logarithm of 100
y = log10(100)   # y = (2+0j)                                      Return the base-10 logarithm of 100

##############################################################

from math import *     #I get the math module fonctions back with reimport.
