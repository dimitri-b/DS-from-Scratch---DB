# coding: utf-8

# change default integer division in 2.7
from __future__ import division

# white space is ignored inside brackets
long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 +
                           13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)

# good for better readability
list_of_lists = [
	[1, 2, 3], 
	[4, 5, 6], 
	[7, 8, 9]
								]
								
# back slash allows splitting lines
x=2+\
	3
print(x)

# difference in import –------
match = 3
print(match)

# import the module, module elements must be referenced with re.
import re
print(match) # no conflict, but see below
x = re.compile("\d{3}")

# same, with an alias
import re as regex
x = regex.compile("\d{3}")

# import one or more elements, which can be referenced directly
from re import compile
x = compile("\d{3}")

# import everything
from re import *
# re has its own match, and with * it overwrites whole namespace 
print(match)
# DON'T DO THIS

# arithmetics -------------
print(5/2)
print(5//2) # integer division


# functions ---------------

def double_it(x):
	 return x*2

y = double_it(5)
print(y)

# functions can be passed to other functions as variables
def apply_func(f):
	# apply the passed in function f to 3
	 return f(3)

y = apply_func(double_it)
print(y)

# functions can be stored in variables
fd = double_it
y = apply_func(fd)


# lambda - short inline functions
y = apply_func(lambda x: x*2)
print(y)
'''
function is defined on the fly, inside the brackets
'''

# default parameters (default must be after non-default)
def apply_func_2(f,x=3):
	 return f(x)

# by position
print(apply_func_2(fd,5))
# by name
print(apply_func_2(fd,x=5))
# default
print(apply_func_2(fd))

# strings ----------------
x = "abc"
# special characters
t = "\t" # tab
s = r"\t" # as is, raw
print(x,t,s)

# multi-line string
multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""

# exceptions ---------------

try:
    print 0 / 0
except ZeroDivisionError:
    print "cannot divide by zero"


# lists ------------------

integer_list = [1, 2, 3]
hetero_list = ["string", 0.1, True]
list_of_lists = [ 
	integer_list, 
	hetero_list, 
	[] 						
								]

list_length = len(integer_list)     
# equals 3
list_sum    = sum(integer_list)

# addressing list elements
x = range(10)   # is the list [0, 1, ..., 9]
zero = x[0]     # equals 0, lists are 0-indexed
one = x[1]      # equals 1
nine = x[-1]    # equals 9, 'Pythonic' for last element
eight = x[-2]   # equals 8, 'Pythonic' for next-to-last element
x[0] = -1       # now x is [-1, 1, 2, 3, ..., 9]

# slicing lists
first_three   = x[:3]   # [-1, 1, 2]
three_to_end = x[3:]    # [3, 4, ..., 9]
one_to_four = x[1:5]    # [1, 2, 3, 4]
last_three = x[-3:]     # [7, 8, 9]
without_first_and_last = x[1:-1]    # [1, 2, ..., 8]
copy_of_x = x[:]   # [-1, 1, 2, ..., 9]

# check if element is in the list
print(1 in [1,2,3])



