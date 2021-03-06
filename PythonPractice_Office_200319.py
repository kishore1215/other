print("Radha Soami")
print('I will prefer using visual studio code as preferred ide for my data science learning')
print('radhasoami')
import pandas as pd
print('importing pandas completed')
"""
before this date, I tried to practice python in jupyter notbook. 
have a feeling now that practicing in vs code will be more beneficial 
since i want to master git also. 
"""
print('above text in code is to test multi-line commenting')
# x +=1 is short hand for x = x + 1
# Handle exceptions with a try/except block 
try:
    #use "raise" to raise an error
    raise IndexError('This is an IndexError')
except IndexError as e:
    pass
except (TypeError, NameError):
    pass
else:
    # optional clause to try/except block must follow all except blocks
    print('All Good!')
finally:
    print('we can clean up all resources here')

"""
*********************************************************************************************
An Iterable is a python fundamental abstraction, an object that can be treated as a sequence.
The object returned from the range function is an iterable.
we can loop over it 
we can not address elements by Index. raises a TypeError
An Iterable is an object that knows how to create an iterator.
for e.g our_iterator = iter(our_iterable)
Our iterator is an object that can remember the state as we traverse through it.
It maintains state as we iterate.
after iterator has returned all of its data, it gives you a StopIteration exceptions.
You can grab all the elements of an iterator by calling list() on it. 
********************************************************************************************

"""
print('above small text is about iterables & iterators')



"""
**********************************************************************************************
Functions
**********************************************************************************************
use def to create new functions 
return values with a return statement
"""
def add(x,y):
    print(" x is {} and y is {}" .format(x,y))
    return x + y

#call functions with parameters 
k = add (4,6)
print(k)
#call functions with keyword arguments 
k = add ( y = 6, x = 4)
print(k)

# define functions that take a variable number of poistional arguments
def varargs(*args):
    return args

k = varargs(1,2,3)
print(k)

# define functions that can take variable number of keyword arguments
def keyword_args(**kwargs):
    return kwargs

p = keyword_args( big = 'foot', loch = 'ness')
print(p)

# you can do both at once, if you like
def all_the_args (*args, **kwargs):
    print(args)
    print(kwargs)

all_the_args( 1, 2,7,9, a = 3, b = 4)

"""
when calling functions, you can do the opposite of args/kwargs!
use * to expand tuples and use ** to expand kwargs
"""
args = (1, 2, 3, 4)
kwargs = {"a" :3, "b" : 4}

all_the_args(*args)
all_the_args(**kwargs)
all_the_args(*args, **kwargs)

# the above function is not clearly understood by me. don't know why *args is not appearing in output.

#you can return multiple values with tuple assignments
#local variable x is not the same as global variable x
#anonymous functions : e.g lambda function
z = (lambda x,y : x**2 +y**2)(2,4)
print(z)

"""
***************
Modules 
***************
you can import Modules
you can get specific functions from a module 
you can import all functions from a module ( not recommended)
you can shorten module names e.g import pandas as pd
python modules are just ordinary python files. you can write your own and import them. 
the name of the module is the same as name of the file. 

if you have a python script named math.py in the same folder as your current script, 
the file math.py will be loaded instead of the built in python module. 
local folder has priority over python's built-in libraries. 

**************
Classes
**************
use the "class" operator to get a class
a class attribute , is chared by all instances of this class 
basic initializer, this is called when class is instantiated. 
note that double leading and trailing underscores denote objects or attributes that are used by pyton 
    but that live in user controlled name spaces. 
Methods ( or objects or attributes ) like : __init__, __str__, __repr__ etc are called magic methods 
dont invent such names by your own
an instance method. all methods take "self" as the first argument. 
a class method is shared among all instances. 
They are called with the calling class as the first argument @classmethod
"""

# a static method is called without a class or instance reference @staticmethod

def grunt():
    return "*grunt*"

x = grunt()
print(x)
"""
a property is just like a getter. 
It turns the method age() into an read-only attribute of the same name. 
This allows property to be set and to be deleted. 
"""
@property

def age(self):
    return self._age

@age.setter

def age(self, age):
    self._age = 41

x = age()

print(x)
