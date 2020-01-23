# if we use * it is tough to figure out which module a function came from

print('namespace 1 :', dir())

"""
from math import *
print('namespace 2: ', dir())
print(sqrt(144))

from cmath import *
print('namespace 3: ', dir())
print(sqrt(144))
"""


# let's import specific functions - but still imported ones could collide with similar named functions in our code
"""
from math import sqrt, pow
print('namespace 2: ', dir())
print(sqrt(144))
"""

# a suggested way is to import just the module - but the catch is that we need to use
# module name every time we use functions
import math
print('namespace_2:', dir())
print(math.sqrt(144))

