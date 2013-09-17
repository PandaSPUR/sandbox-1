#/////////////////////////////////////////////////////////////////////////////////
#
#   Dominic Spinosa
#   Application Security
#   Assignment 1 - Turing Complete Sandbox
#   9/12/13
#   
#   This program acts as a sandbox that feeds the provided (input) program line
#   by line while checking that the potentially executed functions reside within
#   a dictionary of whitelisted functions, which act as a "safe" subset of the
#   Python language. Functions that are not members of the whitelist dictionary
#   are excluded from the built-in set of functions while the program is being
#   executed via the 'exec' function. It also limits the stack and incurred data
#   type(s) memory in order to avoid overflows. 
#
#/////////////////////////////////////////////////////////////////////////////////

import sys
import math
import inspect
import resource

# Set a global limit for the amount of memory allcoated to the stack (256MB) and
# incurred data types (128MB) in order to avoid buffer/data type overflows
STACKMEMORYLIMIT = 256 * 1024
DATAMEMORYLIMIT = 128 * 1024

resource.setrlimit(resource.RLIMIT_STACK,(STACKMEMORYLIMIT,STACKMEMORYLIMIT))
resource.setrlimit(resource.RLIMIT_DATA,(DATAMEMORYLIMIT,DATAMEMORYLIMIT))

# Create array of whitelisted functions, all other functions will be prohibited
whitelist = ['math','acos', 'asin', 'atan', 'atan2', 'ceil',
             'cos', 'cosh', 'e', 'exp', 'fabs',
             'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log',
             'log10', 'modf', 'pi', 'pow', 'radians', 'sin',
             'sinh', 'sqrt', 'tan', 'tanh']

# Convert whitelist array into dictionary to feed into 'exec' argument
whitelist = dict([(dict_element, locals().get(dict_element, None))
                   for dict_element in whitelist])

# Execute provided code line by line using the 'exec' function.
for line in sys.stdin:
    try:
        exec(line, {"__builtins__":None}, whitelist)
    except NameError, e:
        # An undefined or prohibited (non-whitelisted) function as been encountered
        print "ERROR: ", e
    except ImportError, e:
        # User has attempted to import an unwanted/unknown module
        print "ERROR: ", e
    except ZeroDivisionError, e:
        # User has attempted to divide by zero
        print "ERROR: ", e
    finally Exception, e:
        # An error other than Name, Import or ZeroDivision has occurred
        print "ERROR: ", e






